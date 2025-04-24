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
    medication_name = serializers.CharField(source='medication.name', read_only=True)
    patient_name = serializers.CharField(source='patient.get_full_name', read_only=True)
    class Meta:
        model = Prescription
        fields = [
            'id',
            'patient',       # still the ID if you need it
            'patient_name',  # human‐readable
            'medication',    # the FK ID
            'medication_name',
            'dose',
            'prescribed_date'
        ]
        

class DispensingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DispensingHistory
        fields = '__all__'

class RestockingAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestockingAlert
        fields = '__all__'

