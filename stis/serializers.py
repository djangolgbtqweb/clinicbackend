from rest_framework import serializers
from .models import STIDiagnosis, STIMedication, STIEducationMaterial, STIFollowUp

class STIDiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = STIDiagnosis
        fields = '__all__'

class STIMedicationSerializer(serializers.ModelSerializer):
    patient_id = serializers.IntegerField(source='diagnosis.patient_id', read_only=True)
    class Meta:
        model = STIMedication
        fields = ['id', 'diagnosis', 'patient_id', 'medication_name', 'dosage', 'duration']


class STIEducationMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = STIEducationMaterial
        fields = '__all__'

class STIFollowUpSerializer(serializers.ModelSerializer):
    # bring diagnosis.patient_id up one level:
    patient_id = serializers.IntegerField(source='diagnosis.patient_id', read_only=True)
    sti_type   = serializers.CharField(source='diagnosis.sti_type', read_only=True)

    class Meta:
        model = STIFollowUp
        fields = [
            'id',
            'diagnosis',      # if you still want the nested link
            'patient_id',     # now top-level
            'sti_type',       # pulled from the diagnosis
            'follow_up_date',
            'status',
            'notes',
        ]
        depth = 0
