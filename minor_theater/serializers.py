from rest_framework import serializers
from .models import SurgerySchedule, OperationRecord, EquipmentTracking, PostOpFollowUp

class SurgeryScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurgerySchedule
        fields = '__all__'

class OperationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationRecord
        fields = '__all__'

class EquipmentTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentTracking
        fields = '__all__'

class PostOpFollowUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostOpFollowUp
        fields = '__all__'
