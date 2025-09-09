from rest_framework import serializers
from staff.serializers import StaffMemberSerializer
from staff.models import StaffMember

from .models import EmergencyCase, TriageLog, Referral, FirstAidInventory

# Basic EmergencyCase Serializer
class EmergencyCaseSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)

    class Meta:
        model = EmergencyCase
        fields = '__all__'

# TriageLog with nested EmergencyCase
class TriageLogSerializer(serializers.ModelSerializer):
    # Writeable FK for POST/PUT:
    emergency_case = serializers.PrimaryKeyRelatedField(
        queryset=EmergencyCase.objects.all(),
        write_only=True
    )
    
    # Read-only integer ID for frontend display:
    emergency_case_id = serializers.IntegerField(source='emergency_case.id', read_only=True)
    
    # Nested detailed info for display (optional):
    emergency_case_detail = serializers.SerializerMethodField(read_only=True)

    def get_emergency_case_detail(self, obj):
        return {
            'id': obj.emergency_case.id,
            'patient_name': f"{obj.emergency_case.patient.first_name} {obj.emergency_case.patient.last_name}"
        }

    class Meta:
        model = TriageLog
        fields = [
            'id',
            'emergency_case',         # write-only for input
            'emergency_case_id',      # read-only for output
            'emergency_case_detail',  # read-only nested info
            'triage_notes',
            'triaged_by',
            'triage_time',
        ]
# Referral with nested EmergencyCase
class ReferralSerializer(serializers.ModelSerializer):
    emergency_case = EmergencyCaseSerializer(read_only=True)
    emergency_case_id = serializers.PrimaryKeyRelatedField(
        source='emergency_case',
        write_only=True,
        queryset=EmergencyCase.objects.all()
    )
    referred_by = StaffMemberSerializer(read_only=True)  # for reading staff details
    referred_by_id = serializers.PrimaryKeyRelatedField( # for writing staff id
        source='referred_by',
        write_only=True,
        queryset=StaffMember.objects.all(),
        allow_null=True
    )

    class Meta:
        model = Referral
        fields = [
            'id',
            'emergency_case',    # nested for reads
            'emergency_case_id', # use this for writes
            'referred_by',
            'referred_by_id',
            'facility_name',
            'reason',
            'referred_on',
        ]
        read_only_fields = ['id', 'emergency_case', 'referred_on']


# First Aid Inventory doesn't need nesting
class FirstAidInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstAidInventory
        fields = '__all__'
class EmergencyCaseNestedSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)

    class Meta:
        model = EmergencyCase
        fields = ['id', 'patient_name']

class TriageLogSerializer(serializers.ModelSerializer):
    # read‑only nested object that your React UI can drill into
    emergency_case = EmergencyCaseNestedSerializer(read_only=True)

    # write‑only PK for POST/PUT
    emergency_case_id = serializers.PrimaryKeyRelatedField(
        queryset=EmergencyCase.objects.all(),
        source='emergency_case',
        write_only=True,
    )

    class Meta:
        model = TriageLog
        fields = [
            'id',
            'emergency_case',     # nested for GET
            'emergency_case_id',  # PK for POST
            'triage_notes',
            'triaged_by',
            'triage_time',
        ]