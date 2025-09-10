from rest_framework.response import Response
from django.db import transaction
from django.db.models import Count, Q
from rest_framework import status
from rest_framework import viewsets, filters, status
from .models import Room, RoomAssignment, Equipment, EquipmentBooking, Ward, Bed
from .serializers import RoomSerializer, RoomAssignmentSerializer, EquipmentSerializer, EquipmentBookingSerializer, WardSerializer, BedSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from patients.models import Patient
from rest_framework.response import Response
from .serializers import WardSerializer

class WardViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'name', 'ward_type', 'nursing_station',
        'patients__first_name', 'patients__last_name'
    ]

    def list(self, request, *args, **kwargs):
        """
        List wards with optional compact mode for faster loads.
        """
        compact = request.query_params.get('compact') in ['1', 'true', 'True']
        qs = self.get_queryset()

        search = request.query_params.get('search', '').strip()
        if search:
            qs = qs.filter(
                Q(name__icontains=search) |
                Q(patients__first_name__icontains=search) |
                Q(patients__last_name__icontains=search)
            ).distinct()

        if compact:
            qs = qs.annotate(
                beds_count_anno=Count('beds', distinct=True),
                occupied_count_anno=Count('beds', filter=Q(beds__status='occupied'), distinct=True),
                available_count_anno=Count('beds', filter=Q(beds__status='available'), distinct=True),
    ).values(
        'id', 'name', 'capacity',
        'beds_count_anno', 'occupied_count_anno', 'available_count_anno'
    )

            data = [
        {
            'id': item['id'],
            'name': item['name'],
            'capacity': item.get('capacity'),
            'beds_count': item.get('beds_count_anno', 0),
            'occupied_count': item.get('occupied_count_anno', 0),
            'available_count': item.get('available_count_anno', 0),
        }
        for item in qs
            ]
            return Response(data)

        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def assign_patient(self, request, pk=None):
        """
        Assign a patient to an available bed in the ward.
        """
        ward = self.get_object()
        patient_id = request.data.get('patient_id')

        if not patient_id:
            return Response({'error': 'patient_id required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)

        with transaction.atomic():
            bed = Bed.objects.select_for_update().filter(
                ward=ward, status='available'
            ).first()

            if not bed:
                return Response({'error': 'No available beds'}, status=status.HTTP_400_BAD_REQUEST)

            bed.patients.add(patient)
            bed.status = 'occupied'
            bed.save()

            ward.patients.add(patient)

        beds_count = ward.beds.count()
        occupied_count = ward.beds.filter(status='occupied').count()
        available_count = ward.beds.filter(status='available').count()

        return Response({
            'status': 'patient assigned',
            'beds_count': beds_count,
            'occupied_count': occupied_count,
            'available_count': available_count,
            'patient': {
                'id': patient.id,
                'first_name': patient.first_name,
                'last_name': patient.last_name
            }
        }, status=status.HTTP_200_OK)
    @action(detail=True, methods=['post'], url_path='remove_patient')
    def remove_patient(self, request, pk=None):
        """
        Remove a patient from the ward and mark their bed available again.
        """
        ward = self.get_object()
        patient_id = request.data.get('patient_id')

        if not patient_id:
            return Response({'error': 'patient_id required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)

        beds = Bed.objects.filter(ward=ward, patients=patient)
        for bed in beds:
            bed.patients.remove(patient)
            if bed.patients.count() == 0:
                bed.status = 'available'
                bed.save()

        ward.patients.remove(patient)

        beds_count = ward.beds.count()
        occupied_count = ward.beds.filter(status='occupied').count()
        available_count = ward.beds.filter(status='available').count()

        return Response({
        'status': 'patient removed',
        'beds_count': beds_count,
        'occupied_count': occupied_count,
        'available_count': available_count,
        'patient_id': patient.id
    }, status=status.HTTP_200_OK)
    def destroy(self, request, *args, **kwargs):
        return Response(
            {"error": "Deleting wards is not allowed"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['number', 'status', 'ward__name']

    def get_queryset(self):
        qs = super().get_queryset()
        ward_id = self.request.query_params.get('ward')
        if ward_id:
            qs = qs.filter(ward_id=ward_id)
        return qs

    @action(detail=True, methods=['post'])
    def release(self, request, pk=None):
        """Mark bed as available and remove patient assignment."""
        bed = self.get_object()
        bed.status = 'available'
        bed.patients.clear()
        bed.save()
        return Response({'status': 'bed released'}, status=status.HTTP_200_OK)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'room_type', 'status']
class RoomAssignmentViewSet(viewsets.ModelViewSet):
    queryset = RoomAssignment.objects.all()
    serializer_class = RoomAssignmentSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all().order_by('-id')
    serializer_class = EquipmentSerializer

class EquipmentBookingViewSet(viewsets.ModelViewSet):
    queryset = EquipmentBooking.objects.all()
    serializer_class = EquipmentBookingSerializer

class ResourceEquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.filter(used_in='resource').order_by('-id')  # use some field to filter
    serializer_class = EquipmentSerializer

    def perform_create(self, serializer):
        # Automatically tag new equipment as used in resource management
        serializer.save(used_in='resource')