# backend/outpatient/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QueueEntryViewSet, ConsultationRecordViewSet, ReferralViewSet

router = DefaultRouter()
router.register(r'queue', QueueEntryViewSet)
router.register(r'consultations', ConsultationRecordViewSet, basename='consultationrecord')
router.register(r'referrals', ReferralViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Ensure that the router is included at the root path
]

