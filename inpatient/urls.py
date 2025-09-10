# inpatient/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AdmissionViewSet, WardViewSet, BedViewSet

router = DefaultRouter()
router.register(r'admissions', AdmissionViewSet, basename='admission')
router.register(r'wards', WardViewSet, basename='ward')
router.register(r'beds', BedViewSet, basename='bed')

urlpatterns = [
    path('', include(router.urls)),
]

