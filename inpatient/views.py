# inpatient/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction

from .models import Admission
from .serializers import AdmissionSerializer

from outpatient.models import ConsultationRecord
from resource_management.models import Bed, Ward
from patients.models import Patient

from resource_management.serializers import WardSerializer, BedSerializer

# You can change permission_classes to IsAuthenticated for production
from rest_framework.permissions import AllowAny

class WardViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.query_params.get("compact") == "1":
            from inpatient.serializers import WardCompactSerializer
            return WardCompactSerializer
        return super().get_serializer_class()
class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    permission_classes = [AllowAny]


class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all().select_related('consultation', 'patient', 'ward', 'bed')
    serializer_class = AdmissionSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        consultation_id = data.get('consultation')
        ward_id = data.get('ward')
        bed_id = data.get('bed', None)
        reason = data.get('reason', '')

        if not consultation_id or not ward_id:
            return Response({'error': 'consultation and ward are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            consultation = ConsultationRecord.objects.select_related('queue_entry__patient').get(id=consultation_id)
        except ConsultationRecord.DoesNotExist:
            return Response({'error': 'Consultation not found'}, status=status.HTTP_404_NOT_FOUND)

        patient = consultation.queue_entry.patient

        try:
            ward = Ward.objects.get(id=ward_id)
        except Ward.DoesNotExist:
            return Response({'error': 'Ward not found'}, status=status.HTTP_404_NOT_FOUND)

        with transaction.atomic():
            admission = Admission.objects.create(
                consultation=consultation,
                patient=patient,
                ward=ward,
                reason=reason
            )

            assigned_bed = None

            if bed_id:
                # Assign explicit bed if provided
                try:
                    bed = Bed.objects.select_for_update().get(id=bed_id, ward=ward)
                except Bed.DoesNotExist:
                    return Response({'error': 'Bed not found in this ward'}, status=status.HTTP_400_BAD_REQUEST)

                if bed.status != 'available':
                    return Response({'error': 'Bed already occupied'}, status=status.HTTP_400_BAD_REQUEST)

                admission.assign_bed(bed, save=True)
                assigned_bed = bed
            else:
                # Auto-assign first available bed in the ward
                bed = Bed.objects.select_for_update().filter(ward=ward, status='available').first()
                if bed:
                    admission.assign_bed(bed, save=True)
                    assigned_bed = bed
                else:
                    # No bed available — admission remains pending
                    admission.save()

            # Optionally mark queue/consultation status to completed
            try:
                qe = consultation.queue_entry
                qe.status = 'completed'
                qe.save()
            except Exception:
                pass

            serializer = self.get_serializer(admission)
            resp = serializer.data

            if assigned_bed:
                resp['bed_id'] = assigned_bed.id
                resp['bed_label'] = getattr(assigned_bed, 'label', None)

            # include ward counts to help frontend update compact list
            try:
                beds_count = ward.beds.count()
                occupied_count = ward.beds.filter(status='occupied').count()
                available_count = ward.beds.filter(status='available').count()
            except Exception:
                beds_count = occupied_count = available_count = None

            resp['beds_count'] = beds_count
            resp['occupied_count'] = occupied_count
            resp['available_count'] = available_count

            return Response(resp, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def assign_bed(self, request, pk=None):
        """
        Assign a bed to an existing admission (e.g., from a pending admission).
        Payload: { "bed": <bed_id> }
        """
        admission = self.get_object()
        bed_id = request.data.get('bed')
        if not bed_id:
            return Response({'error': 'bed id required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            bed = Bed.objects.select_for_update().get(id=bed_id, ward=admission.ward)
        except Bed.DoesNotExist:
            return Response({'error': 'Bed not found in this ward'}, status=status.HTTP_404_NOT_FOUND)

        if bed.status != 'available':
            return Response({'error': 'Bed not available'}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            admission.assign_bed(bed, save=True)

            resp = self.get_serializer(admission).data
            resp['bed_id'] = bed.id
            resp['bed_label'] = getattr(bed, 'label', None)

            # ward counts
            try:
                ward = admission.ward
                resp['beds_count'] = ward.beds.count()
                resp['occupied_count'] = ward.beds.filter(status='occupied').count()
                resp['available_count'] = ward.beds.filter(status='available').count()
            except Exception:
                pass

            return Response(resp, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def discharge(self, request, pk=None):
        """
        Discharge an admitted patient. Frees the bed and marks admission discharged.
        """
        admission = self.get_object()
        if admission.status != 'admitted' or not admission.bed:
            return Response({'error': 'Admission not currently admitted or missing bed'}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            # lock the bed row
            bed = Bed.objects.select_for_update().get(id=admission.bed.id)
            # remove patient from bed and update bed status
            try:
                bed.patients.remove(admission.patient)
                if bed.patients.count() == 0:
                    bed.status = 'available'
                    bed.save()
            except Exception:
                bed.status = 'available'
                bed.save()

            admission.status = 'discharged'
            admission.save()

            return Response({'status': 'discharged'}, status=status.HTTP_200_OK)
