from rest_framework import serializers
from patients.models import Patient
from .models import Disease, FollowUp

# backend/chronic_disease_management/serializers.py

from rest_framework import serializers
from patients.models import Patient
from .models import Disease, FollowUp

class PatientNameSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Patient
        fields = ['first_name', 'last_name']


class DiseaseSerializer(serializers.ModelSerializer):
    # allow writing the FK by ID
    patient = PatientNameSerializer(read_only=True)
    # still expose the full name read‑only
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)

    class Meta:
        model  = Disease
        fields = [
            'id',
            'patient',       # writeable FK
            'patient_name',  # read‑only display
            'disease_type',
            'diagnosis_date',
            'treatment_plan',
            'status',
        ]


class FollowUpSerializer(serializers.ModelSerializer):
    # nest the Disease for reads
    disease    = DiseaseSerializer(read_only=True)
    # allow submitting a follow‑up by disease ID
    disease_id = serializers.PrimaryKeyRelatedField(
        source='disease',  # maps to the model’s FK
        queryset=Disease.objects.all(),
        write_only=True
    )

    class Meta:
        model  = FollowUp
        fields = [
            'id',
            'disease',    # the nested read‑only block
            'disease_id', # the FK field you POST
            'follow_up_date',
            'notes',
        ]
# serializers.py

class DiseaseSummarySerializer(serializers.ModelSerializer):
    patient = PatientNameSerializer(read_only=True)

    class Meta:
        model = Disease
        fields = ['id', 'disease_type', 'patient']

class FollowUpSerializer(serializers.ModelSerializer):
    disease = DiseaseSummarySerializer(read_only=True)
    disease_id = serializers.PrimaryKeyRelatedField(queryset=Disease.objects.all(), write_only=True, source='disease')

    class Meta:
        model = FollowUp
        fields = ['id', 'disease', 'disease_id', 'follow_up_date', 'notes']
