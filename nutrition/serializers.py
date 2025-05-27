from rest_framework import serializers
from .models import DietaryAssessment, MealPlan, SupplementPrescription, ProgressMonitor

class DietaryAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietaryAssessment
        fields = '__all__'

class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = '__all__'


class SupplementPrescriptionSerializer(serializers.ModelSerializer):
    patient_id = serializers.SerializerMethodField()
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = SupplementPrescription
        fields = ['id', 'patient_id', 'patient_name', 'supplement_name', 'dosage', 'duration']

    def get_patient_id(self, obj):
        return obj.patient.id if obj.patient else None

    def get_patient_name(self, obj):
        if obj.patient:
            full_name = obj.patient.full_name
            # If full_name is a method, call it
            if callable(full_name):
                return full_name()
            return full_name
        return "N/A"


from rest_framework import serializers
from .models import ProgressMonitor

class ProgressMonitorSerializer(serializers.ModelSerializer):
    patient_id   = serializers.IntegerField(source='patient.id', read_only=True)
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)

    class Meta:
        model  = ProgressMonitor
        fields = [
            'id',
            'patient_id',
            'patient_name',
            'date',
            'weight',
            'bmi',
            'notes',
        ]


