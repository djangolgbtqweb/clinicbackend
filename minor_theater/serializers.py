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
    patient_name = serializers.CharField(source='surgery.patient.full_name', read_only=True)
    procedure = serializers.CharField(source='surgery.procedure', read_only=True)
    surgeon = serializers.CharField(source='surgery.surgeon', read_only=True)
    assistant = serializers.CharField(source='surgery.assistant', read_only=True)  # Optional, only if model has it

    class Meta:
        model = OperationRecord
        fields = [
            'id',
            'surgery',
            'notes',
            'outcome',
            'performed_by',
            'operation_date',
            'patient_name',
            'procedure',
            'surgeon',
            'assistant',  # Optional
        ]


# --- Equipment Tracking Serializer ---
class EquipmentTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentTracking
        fields = '__all__'


class PostOpFollowUpSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='surgery.patient.full_name', read_only=True)
    procedure    = serializers.CharField(source='surgery.procedure',    read_only=True)
    surgeon_name = serializers.CharField(source='surgery.surgeon', read_only=True)
    status       = serializers.SerializerMethodField()

    class Meta:
        model  = PostOpFollowUp
        fields = [
            'id',
            'surgery',
            'patient_name',
            'procedure',
            'surgeon_name',
            'follow_up_date',
            'notes',
            'attended',
            'status',
        ]

    def get_status(self, obj):
        # derive human‐friendly status
        return 'Completed' if obj.attended else 'Scheduled'