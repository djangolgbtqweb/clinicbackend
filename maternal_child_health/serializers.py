# backend/maternal_child_health/serializers.py
from rest_framework import serializers
from .models import AntenatalPostnatalRecord, VaccinationRecord, GrowthMonitoring, FamilyPlanning
from patients.models import Patient

class AntenatalPostnatalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntenatalPostnatalRecord
        fields = '__all__'

from rest_framework import serializers
from .models import VaccinationRecord

class VaccinationRecordSerializer(serializers.ModelSerializer):
    # incoming writes go into this field:
    patient = serializers.IntegerField(write_only=True)
    # outgoing reads use this field:
    patient_id = serializers.IntegerField(source='patient.id', read_only=True)

    class Meta:
        model = VaccinationRecord
        fields = [
            'id',
            'patient',     # write-only
            'patient_id',  # read-only
            'vaccine_name',
            'vaccine_date',
            'status',
        ]

    def create(self, validated_data):
        patient_pk = validated_data.pop('patient')
        return VaccinationRecord.objects.create(
            patient_id=patient_pk,
            **validated_data
        )

class GrowthMonitoringSerializer(serializers.ModelSerializer):
    # write-only raw patient PK from frontend
    patient = serializers.IntegerField(write_only=True)
    # read-only for responses
    patient_id = serializers.IntegerField(source='patient.id', read_only=True)

    class Meta:
        model = GrowthMonitoring
        fields = [
            'id',
            'patient',          # write-only
            'patient_id',       # read-only
            'record_date',
            'height',
            'weight',
            'head_circumference',
        ]

    def create(self, validated_data):
        patient_pk = validated_data.pop('patient')
        return GrowthMonitoring.objects.create(
            patient_id=patient_pk,
            **validated_data
        )


class FamilyPlanningSerializer(serializers.ModelSerializer):
    # incoming write-only patient PK
    patient = serializers.IntegerField(write_only=True)
    # outgoing read-only patient ID
    patient_id = serializers.IntegerField(source='patient.id', read_only=True)

    class Meta:
        model = FamilyPlanning
        fields = [
            'id',
            'patient',       # write-only
            'patient_id',    # read-only
            'service_type',
            'service_date',
            'details',
        ]

    def create(self, validated_data):
        patient_pk = validated_data.pop('patient')
        return FamilyPlanning.objects.create(
            patient_id=patient_pk,
            **validated_data
        )
