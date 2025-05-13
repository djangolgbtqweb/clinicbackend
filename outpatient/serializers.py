# backend/outpatient/serializers.py
from rest_framework import serializers
from .models import QueueEntry, ConsultationRecord, Referral

class QueueEntrySerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)
    class Meta:
        model = QueueEntry
        fields = ['id', 'patient', 'patient_name', 'status', 'priority', 'arrived_at']

class ConsultationRecordSerializer(serializers.ModelSerializer):
    # Expose `patient` name via the related queue_entry
    patient_name = serializers.CharField(
        source='queue_entry.patient.full_name', 
        read_only=True
    )

    class Meta:
        model  = ConsultationRecord
        # Only these fields are needed for list/create
        fields = [
            'id',
            'queue_entry',
            'patient_name',
            'doctor_name',
            'symptoms',
            'diagnosis',
            'prescriptions',
            'notes',
            'consulted_at',
        ]

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = '__all__'
