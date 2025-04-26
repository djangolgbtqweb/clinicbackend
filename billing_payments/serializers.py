from rest_framework import serializers
from .models import Service, Invoice, Payment

class ServiceSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ['id', 'patient', 'patient_name', 'name', 'price']

    def get_patient_name(self, obj):
        # str(obj.patient) calls Patient.__str__(), which should be the patient's name
        return str(obj.patient) if obj.patient else None
class InvoiceSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = ['id', 'patient', 'patient_name', 'date', 'services', 'total_amount', 'paid']

    def get_patient_name(self, obj):
        # uses Patient.__str__(), e.g. "John Doe (DOB: …)"
        return str(obj.patient) if obj.patient else None

class PaymentSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        # Make sure to include 'patient_name'
        fields = ['id', 'invoice', 'patient_name', 'date', 'amount_paid', 'payment_method']

    def get_patient_name(self, obj):
        # Uses Invoice → Patient relationship
        return str(obj.invoice.patient) if obj.invoice and obj.invoice.patient else None
