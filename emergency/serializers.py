from rest_framework import serializers
from .models import EmergencyCase, TriageLog, Referral, FirstAidInventory

# Basic EmergencyCase Serializer
class EmergencyCaseSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)

    class Meta:
        model = EmergencyCase
        fields = '__all__'

# TriageLog with nested EmergencyCase
class TriageLogSerializer(serializers.ModelSerializer):
    # Keep the nested read-only if you like:
    emergency_case_detail = serializers.SerializerMethodField(read_only=True)

    # Add this writeable PK field:
    emergency_case = serializers.PrimaryKeyRelatedField(
        queryset=EmergencyCase.objects.all(),
        write_only=True
    )

    def get_emergency_case_detail(self, obj):
        return {
            'id': obj.emergency_case.id,
            'patient_name': f"{obj.emergency_case.patient.first_name} {obj.emergency_case.patient.last_name}"
        }

    class Meta:
        model = TriageLog
        fields = [
            'id',
            'emergency_case',            # writeable FK
            'emergency_case_detail',     # nested read-only
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

    class Meta:
        model = Referral
        fields = [
            'id',
            'emergency_case',    # nested for reads
            'emergency_case_id', # use this for writes
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