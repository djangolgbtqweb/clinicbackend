# backend/maternal_child_health/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AntenatalPostnatalRecordViewSet, VaccinationRecordViewSet, GrowthMonitoringViewSet, FamilyPlanningViewSet

router = DefaultRouter()
router.register(r'antenatal-postnatal', AntenatalPostnatalRecordViewSet)
router.register(r'vaccinations', VaccinationRecordViewSet)
router.register(r'growth-monitoring', GrowthMonitoringViewSet)
router.register(r'family-planning', FamilyPlanningViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
