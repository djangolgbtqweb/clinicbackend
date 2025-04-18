from rest_framework import viewsets
from .models import EmergencyCase, TriageLog, Referral, FirstAidInventory
from .serializers import EmergencyCaseSerializer, TriageLogSerializer, ReferralSerializer, FirstAidInventorySerializer

class EmergencyCaseViewSet(viewsets.ModelViewSet):
    queryset = EmergencyCase.objects.all()
    serializer_class = EmergencyCaseSerializer

class TriageLogViewSet(viewsets.ModelViewSet):
    queryset = TriageLog.objects.all()
    serializer_class = TriageLogSerializer

class ReferralViewSet(viewsets.ModelViewSet):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer

class FirstAidInventoryViewSet(viewsets.ModelViewSet):
    queryset = FirstAidInventory.objects.all()
    serializer_class = FirstAidInventorySerializer

