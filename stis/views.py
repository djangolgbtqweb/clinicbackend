from rest_framework import viewsets
from .models import STIDiagnosis, STIMedication, STIEducationMaterial, STIFollowUp
from .serializers import (
    STIDiagnosisSerializer,
    STIMedicationSerializer,
    STIEducationMaterialSerializer,
    STIFollowUpSerializer,
)

class STIDiagnosisViewSet(viewsets.ModelViewSet):
    queryset = STIDiagnosis.objects.all()
    serializer_class = STIDiagnosisSerializer

class STIMedicationViewSet(viewsets.ModelViewSet):
    queryset = STIMedication.objects.all()
    serializer_class = STIMedicationSerializer

class STIEducationMaterialViewSet(viewsets.ModelViewSet):
    queryset = STIEducationMaterial.objects.all()
    serializer_class = STIEducationMaterialSerializer

class STIFollowUpViewSet(viewsets.ModelViewSet):
    queryset = STIFollowUp.objects.all()
    serializer_class = STIFollowUpSerializer
