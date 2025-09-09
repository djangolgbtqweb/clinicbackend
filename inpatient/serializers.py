# inpatient/serializers.py
from rest_framework import serializers
from .models import Admission

class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = [
            'id', 'consultation', 'patient', 'ward', 'bed',
            'reason', 'status', 'admitted_at', 'created_at', 'admitted_by'
        ]
        read_only_fields = ['id', 'admitted_at', 'created_at', 'status', 'patient']
