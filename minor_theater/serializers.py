from rest_framework import serializers
from .models import SurgerySchedule, OperationRecord, EquipmentTracking, PostOpFollowUp
from patients.models import Patient

# --- Patient Serializer ---
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'full_name']


# --- Surgery Schedule Serializer ---
class SurgeryScheduleSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)  # for GET
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), write_only=True
    )  # for POST/PUT

    class Meta:
        model = SurgerySchedule
        fields = [
            'id',
            'patient',
            'patient_id',  # <- must include this
            'scheduled_date',
            'surgeon',
            'procedure',
            'status',
        ]

    def create(self, validated_data):
        # Pop out patient_id and assign to patient
        validated_data['patient'] = validated_data.pop('patient_id')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'patient_id' in validated_data:
            validated_data['patient'] = validated_data.pop('patient_id')
        return super().update(instance, validated_data)



# --- Operation Record Serializer ---
class OperationRecordSerializer(serializers.ModelSerializer):
    # accept surgery=<id> on POST
    surgery = serializers.PrimaryKeyRelatedField(
        queryset=SurgerySchedule.objects.all(),
        write_only=True
    )
    # return full nested surgery (which itself nests patient)
    surgery_detail = SurgeryScheduleSerializer(
        source='surgery',
        read_only=True
    )
    # convenience fields (optional)
    patient_id   = serializers.IntegerField(source='surgery.patient.id',           read_only=True)
    patient_name = serializers.CharField(   source='surgery.patient.full_name',    read_only=True)
    procedure    = serializers.CharField(   source='surgery.procedure',           read_only=True)
    surgeon      = serializers.CharField(   source='surgery.surgeon',             read_only=True)
    assistant    = serializers.CharField(   source='surgery.assistant',           read_only=True)

    class Meta:
        model = OperationRecord
        fields = [
            'id',
            'surgery',         # write-only PK for POST
            'surgery_detail',  # read-only nested object for GET
            'performed_by',
            'outcome',
            'operation_date',
            'notes',
            # optional convenience fields
            'patient_id',
            'patient_name',
            'procedure',
            'surgeon',
            'assistant',
        ]


# --- Equipment Tracking Serializer ---
class EquipmentTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentTracking
        fields = '__all__'


# --- Post-Op Follow-Up Serializer ---
class SurgeryScheduleSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(    # for POST
        queryset=Patient.objects.all(),
        write_only=True
    )

    class Meta:
        model  = SurgerySchedule
        fields = ['id', 'patient', 'patient_id', 'scheduled_date', 'surgeon', 'procedure', 'status']
        
    def create(self, validated_data):
        # move patient_id → patient FK
        validated_data['patient'] = validated_data.pop('patient_id')
        return super().create(validated_data)

class PostOpFollowUpSerializer(serializers.ModelSerializer):
    # Writeable PK for creating/updating
    surgery = serializers.PrimaryKeyRelatedField(
        queryset=SurgerySchedule.objects.all(),
        write_only=True
    )
    # Read-only nested detail for GET
    surgery_detail = SurgeryScheduleSerializer(source='surgery', read_only=True)

    # Convenience read-only fields
    patient_name = serializers.CharField(source='surgery.patient.full_name', read_only=True)
    procedure    = serializers.CharField(source='surgery.procedure',         read_only=True)
    surgeon_name = serializers.CharField(source='surgery.surgeon',          read_only=True)
    status       = serializers.SerializerMethodField()

    class Meta:
        model  = PostOpFollowUp
        fields = [
            'id',
            'surgery',         # write-only PK
            'surgery_detail',  # read-only nested
            'patient_name',    # convenience
            'procedure',
            'surgeon_name',
            'follow_up_date',
            'notes',
            'attended',
            'status',
        ]

    def get_status(self, obj):
        return 'Completed' if obj.attended else 'Scheduled'
