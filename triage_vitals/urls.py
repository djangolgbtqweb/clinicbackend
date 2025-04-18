from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TriageViewSet, VitalSignViewSet

router = DefaultRouter()
router.register(r'triage', TriageViewSet)
router.register(r'vitals', VitalSignViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
