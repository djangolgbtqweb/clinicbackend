from rest_framework import viewsets
from .models import SurgerySchedule, OperationRecord, EquipmentTracking, PostOpFollowUp
from .serializers import SurgeryScheduleSerializer, OperationRecordSerializer, EquipmentTrackingSerializer, PostOpFollowUpSerializer

class SurgeryScheduleViewSet(viewsets.ModelViewSet):
    queryset = SurgerySchedule.objects.all()
    serializer_class = SurgeryScheduleSerializer

class OperationRecordViewSet(viewsets.ModelViewSet):
    queryset = OperationRecord.objects.all()
    serializer_class = OperationRecordSerializer

class EquipmentTrackingViewSet(viewsets.ModelViewSet):
    queryset = EquipmentTracking.objects.all()
    serializer_class = EquipmentTrackingSerializer

class PostOpFollowUpViewSet(viewsets.ModelViewSet):
    queryset = PostOpFollowUp.objects.all()
    serializer_class = PostOpFollowUpSerializer
