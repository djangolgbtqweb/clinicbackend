from rest_framework import viewsets
from .models import Patient, Appointment, TestResult
from .serializers import PatientSerializer, AppointmentSerializer, TestResultSerializer
from .serializers import TestResultSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('last_name', 'first_name')
    serializer_class = PatientSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset         = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer
    
