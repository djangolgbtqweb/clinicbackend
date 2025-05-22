# backend/patients/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, AppointmentViewSet, TestResultViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'appointments', AppointmentViewSet, basename='appointment')
router.register(r'test-results', TestResultViewSet, basename='testresult')

urlpatterns = [
    path('', include(router.urls)),
]


