from rest_framework import serializers
from .models import STIDiagnosis, STIMedication, STIEducationMaterial, STIFollowUp

class STIDiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = STIDiagnosis
        fields = '__all__'

class STIMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = STIMedication
        fields = '__all__'

class STIEducationMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = STIEducationMaterial
        fields = '__all__'

class STIFollowUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = STIFollowUp
        fields = '__all__'
