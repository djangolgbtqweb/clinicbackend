# backend/outpatient/views.py
from rest_framework import viewsets
from .models import QueueEntry, ConsultationRecord, Referral
from .serializers import QueueEntrySerializer, ConsultationRecordSerializer, ReferralSerializer

class QueueEntryViewSet(viewsets.ModelViewSet):
    queryset = QueueEntry.objects.all()
    serializer_class = QueueEntrySerializer

class ConsultationRecordViewSet(viewsets.ModelViewSet):
    queryset = ConsultationRecord.objects.all()
    serializer_class = ConsultationRecordSerializer

class ReferralViewSet(viewsets.ModelViewSet):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer
