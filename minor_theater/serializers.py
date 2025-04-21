from rest_framework import serializers
from .models import SurgerySchedule, OperationRecord, EquipmentTracking, PostOpFollowUp

# --- Surgery Schedule Serializer ---
class SurgeryScheduleSerializer(serializers.ModelSerializer):
    # Assumes 'patient' is a ForeignKey in SurgerySchedule to a Patient model
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)

    class Meta:
        model = SurgerySchedule
        fields = ['id', 'patient', 'scheduled_date', 'surgeon', 'procedure', 'status', 'patient_name']


# --- Operation Record Serializer ---
class OperationRecordSerializer(serializers.ModelSerializer):
    # Assuming there's a related patient field, replace it with actual field if needed
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)

    class Meta:
        model = OperationRecord
        fields = ['id', 'patient', 'surgeon', 'procedure', 'date', 'notes', 'status', 'patient_name']


# --- Equipment Tracking Serializer ---
class EquipmentTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentTracking
        fields = '__all__'


# --- Post-Op Follow-Up Serializer ---
class PostOpFollowUpSerializer(serializers.ModelSerializer):
    # Correcting extra field definition
    patient_name = serializers.CharField(source='surgery.patient.full_name', read_only=True)
    procedure = serializers.CharField(source='surgery.procedure', read_only=True)

    class Meta:
        model = PostOpFollowUp
        fields = '__all__'  # We don't need to manually append extra fields here
