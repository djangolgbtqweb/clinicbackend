from rest_framework import viewsets
from .models import Triage, VitalSign
from .serializers import TriageSerializer, VitalSignSerializer

class TriageViewSet(viewsets.ModelViewSet):
    queryset = Triage.objects.all()
    serializer_class = TriageSerializer

class VitalSignViewSet(viewsets.ModelViewSet):
    queryset = VitalSign.objects.all()
    serializer_class = VitalSignSerializer

