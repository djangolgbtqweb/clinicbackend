from rest_framework import serializers
from patients.models import Patient
from .models import Disease, FollowUp

# Patient name serializer
class PatientNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name']

# Disease with nested patient, diagnosis_date, and status
class DiseaseSerializer(serializers.ModelSerializer):
    patient = PatientNameSerializer(read_only=True)

    class Meta:
        model = Disease
        fields = ['id', 'disease_type', 'patient', 'diagnosis_date', 'status']

# Follow-up with nested disease (which contains patient)
class FollowUpSerializer(serializers.ModelSerializer):
    disease = DiseaseSerializer(read_only=True)

    class Meta:
        model = FollowUp
        fields = ['id', 'disease', 'follow_up_date', 'notes']
