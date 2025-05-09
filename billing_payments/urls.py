from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, InvoiceViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
