# backend/maternal_child_health/serializers.py
from rest_framework import serializers
from .models import AntenatalPostnatalRecord, VaccinationRecord, GrowthMonitoring, FamilyPlanning

class AntenatalPostnatalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntenatalPostnatalRecord
        fields = '__all__'

class VaccinationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationRecord
        fields = '__all__'

class GrowthMonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrowthMonitoring
        fields = '__all__'

class FamilyPlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyPlanning
        fields = '__all__'
