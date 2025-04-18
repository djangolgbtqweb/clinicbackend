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
    class Meta:
        model = SupplementPrescription
        fields = '__all__'

class ProgressMonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressMonitor
        fields = '__all__'
