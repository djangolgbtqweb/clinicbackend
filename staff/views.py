from rest_framework import viewsets
from .models import StaffMember, DutyRoster, LeaveRequest, OnCallSchedule
from .serializers import StaffMemberSerializer, DutyRosterSerializer, LeaveRequestSerializer, OnCallScheduleSerializer

class StaffMemberViewSet(viewsets.ModelViewSet):
    queryset = StaffMember.objects.all()
    serializer_class = StaffMemberSerializer

class DutyRosterViewSet(viewsets.ModelViewSet):
    queryset = DutyRoster.objects.all()
    serializer_class = DutyRosterSerializer

class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer

class OnCallScheduleViewSet(viewsets.ModelViewSet):
    queryset = OnCallSchedule.objects.all()
    serializer_class = OnCallScheduleSerializer

