# patients/serializers.py
from rest_framework import serializers
from patients.models import TestResult, Appointment

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = ['test_name', 'result', 'date_of_test', 'technician_name']  # Ensure these fields exist

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'doctor_name', 'purpose_of_visit']  # Ensure these fields exist

