# backend/outpatient/serializers.py
from rest_framework import serializers
from .models import QueueEntry, ConsultationRecord, Referral

class QueueEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueEntry
        fields = '__all__'

class ConsultationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationRecord
        fields = '__all__'

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = '__all__'
