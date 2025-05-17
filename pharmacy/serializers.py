from rest_framework import serializers
from .models import Medication, Prescription, DispensingHistory, RestockingAlert

class MedicationSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Medication
        fields = '__all__'  # or you can specify the fields you want to include

    def get_total_cost(self, obj):
        return obj.quantity * obj.price_per_unit

class PrescriptionSerializer(serializers.ModelSerializer):
    medication_name = serializers.CharField(
        source='medication.name', 
        read_only=True
    )
    patient_name = serializers.CharField(
        source='patient.full_name',  # ← add this
        read_only=True
    )

    class Meta:
        model = Prescription
        fields = [
            'id',
            'patient',
            'patient_name',
            'medication',
            'medication_name',
            'dose',
            'prescribed_date',
        ]
        

class DispensingHistorySerializer(serializers.ModelSerializer):
    prescription_id  = serializers.IntegerField(source='prescription.id',              read_only=True)
    patient_name     = serializers.CharField( source='prescription.patient.full_name', read_only=True)
    medication_name  = serializers.CharField( source='prescription.medication.name',   read_only=True)
    medication_id    = serializers.IntegerField(source='prescription.medication.id',   read_only=True)  # new

    class Meta:
        model = DispensingHistory
        fields = [
            'id',
            'prescription',     # writeable FK
            'prescription_id',
            'patient_name',
            'medication_id',    # include here
            'medication_name',
            'dispense_date',
            'quantity_dispensed',
        ]

class RestockingAlertSerializer(serializers.ModelSerializer):
    # Read‑only human name for the related medication
    medication_name = serializers.CharField(
        source='medication.name',
        read_only=True
    )

    class Meta:
        model = RestockingAlert
        fields = [
            'id',
            'medication',         # FK ID
            'medication_name',    # human-readable name
            'threshold_quantity',
            'alert_date',
        ]

