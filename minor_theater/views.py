from rest_framework import viewsets
from .models import SurgerySchedule, OperationRecord, EquipmentTracking, PostOpFollowUp
from .serializers import (
    SurgeryScheduleSerializer,
    OperationRecordSerializer,
    EquipmentTrackingSerializer,
    PostOpFollowUpSerializer,
)

class SurgeryScheduleViewSet(viewsets.ModelViewSet):
    queryset = SurgerySchedule.objects.select_related('patient').all()
    serializer_class = SurgeryScheduleSerializer


class OperationRecordViewSet(viewsets.ModelViewSet):
    queryset = OperationRecord.objects.select_related(
        'surgery',            # bring in the SurgerySchedule object
        'surgery__patient'    # and its Patient
    ).all()
    serializer_class = OperationRecordSerializer


class EquipmentTrackingViewSet(viewsets.ModelViewSet):
    queryset = EquipmentTracking.objects.all()
    serializer_class = EquipmentTrackingSerializer


class PostOpFollowUpViewSet(viewsets.ModelViewSet):
    queryset = PostOpFollowUp.objects.select_related(
        'surgery',
        'surgery__patient'
    ).all()
    serializer_class = PostOpFollowUpSerializer

