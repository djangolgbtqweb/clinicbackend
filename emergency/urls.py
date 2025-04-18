from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmergencyCaseViewSet, TriageLogViewSet, ReferralViewSet, FirstAidInventoryViewSet

router = DefaultRouter()
router.register(r'emergency-cases', EmergencyCaseViewSet)
router.register(r'triage-logs', TriageLogViewSet)
router.register(r'referrals', ReferralViewSet)
router.register(r'first-aid-inventory', FirstAidInventoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
