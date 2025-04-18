# backend/maternal_child_health/views.py
from rest_framework import viewsets
from .models import AntenatalPostnatalRecord, VaccinationRecord, GrowthMonitoring, FamilyPlanning
from .serializers import AntenatalPostnatalRecordSerializer, VaccinationRecordSerializer, GrowthMonitoringSerializer, FamilyPlanningSerializer

class AntenatalPostnatalRecordViewSet(viewsets.ModelViewSet):
    queryset = AntenatalPostnatalRecord.objects.all()
    serializer_class = AntenatalPostnatalRecordSerializer

class VaccinationRecordViewSet(viewsets.ModelViewSet):
    queryset = VaccinationRecord.objects.all()
    serializer_class = VaccinationRecordSerializer

class GrowthMonitoringViewSet(viewsets.ModelViewSet):
    queryset = GrowthMonitoring.objects.all()
    serializer_class = GrowthMonitoringSerializer

class FamilyPlanningViewSet(viewsets.ModelViewSet):
    queryset = FamilyPlanning.objects.all()
    serializer_class = FamilyPlanningSerializer
