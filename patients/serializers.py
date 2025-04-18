from rest_framework import serializers
from .models import Patient, Appointment
from .models import TestResult

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Appointment
        fields = '__all__'
    
class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'
