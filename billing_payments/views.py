from rest_framework import viewsets
from .models import Service, Invoice, Payment
from .serializers import ServiceSerializer, InvoiceSerializer, PaymentSerializer
from django.db.models import Sum

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        # 1) Save the new payment
        payment = serializer.save()

        # 2) Recompute total paid on this invoice
        invoice = payment.invoice
        total_paid = (
            invoice.payment_set.aggregate(sum_paid=Sum('amount_paid'))['sum_paid']
            or 0
        )

        # 3) If total_paid ≥ invoice.total_amount, mark it as paid
        if total_paid >= invoice.total_amount:
            invoice.paid = True
            invoice.save()

    def perform_update(self, serializer):
        # If someone edits a payment (e.g. changes amount_paid), re‐check the invoice.
        payment = serializer.save()
        invoice = payment.invoice
        total_paid = (
            invoice.payment_set.aggregate(sum_paid=Sum('amount_paid'))['sum_paid']
            or 0
        )
        invoice.paid = (total_paid >= invoice.total_amount)
        invoice.save()

