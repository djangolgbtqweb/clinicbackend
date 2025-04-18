# backend/pharmacy/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicationViewSet, PrescriptionViewSet, DispensingHistoryViewSet, RestockingAlertViewSet, TotalCostView

router = DefaultRouter()
router.register(r'medications', MedicationViewSet)
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'dispensing-history', DispensingHistoryViewSet)
router.register(r'restocking-alerts', RestockingAlertViewSet)

urlpatterns = [
    path('', include(router.urls)),  # DO NOT nest this under 'api/pharmacy/' again here
    path('medications/<int:pk>/total-cost/', TotalCostView.as_view(), name='medication-total-cost'),
]


