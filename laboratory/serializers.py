from rest_framework import serializers
from .models import LabTest, SampleTracking, LabResult

class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTest
        fields = '__all__'

class SampleTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleTracking
        fields = '__all__'

class LabResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabResult
        fields = '__all__'
