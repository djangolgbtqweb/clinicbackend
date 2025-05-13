# backend/outpatient/views.py
from rest_framework import viewsets, status, filters
from .models import QueueEntry, ConsultationRecord, Referral
from .serializers import QueueEntrySerializer, ConsultationRecordSerializer, ReferralSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class QueueEntryViewSet(viewsets.ModelViewSet):
    queryset = QueueEntry.objects.all()
    serializer_class = QueueEntrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['patient__first_name', 'patient__last_name']

class ConsultationRecordViewSet(viewsets.ModelViewSet):
    queryset = ConsultationRecord.objects.all()
    serializer_class = ConsultationRecordSerializer

    def create(self, request, *args, **kwargs):
        # Override create to return validation errors if any
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ReferralViewSet(viewsets.ModelViewSet):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer
