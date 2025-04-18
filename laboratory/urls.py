from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LabTestViewSet, SampleTrackingViewSet, LabResultViewSet

router = DefaultRouter()
router.register(r'lab-tests', LabTestViewSet)
router.register(r'sample-tracking', SampleTrackingViewSet)
router.register(r'lab-results', LabResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
