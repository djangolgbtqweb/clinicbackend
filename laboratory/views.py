from rest_framework import viewsets
from .models import LabTest, SampleTracking, LabResult
from .serializers import LabTestSerializer, SampleTrackingSerializer, LabResultSerializer

class LabTestViewSet(viewsets.ModelViewSet):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer

class SampleTrackingViewSet(viewsets.ModelViewSet):
    queryset = SampleTracking.objects.all()
    serializer_class = SampleTrackingSerializer

class LabResultViewSet(viewsets.ModelViewSet):
    queryset = LabResult.objects.all()
    serializer_class = LabResultSerializer
