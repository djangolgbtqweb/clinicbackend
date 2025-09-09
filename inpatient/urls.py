# inpatient/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AdmissionViewSet

router = DefaultRouter()
router.register(r'admissions', AdmissionViewSet, basename='admission')

urlpatterns = [
    path('', include(router.urls)),
]
