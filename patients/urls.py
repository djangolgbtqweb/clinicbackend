# backend/patients/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet

# Create a router and register the ViewSet
router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')

# Include the router URLs
urlpatterns = router.urls

