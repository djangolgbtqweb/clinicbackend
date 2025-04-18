from rest_framework import serializers
from .models import StaffMember, DutyRoster, LeaveRequest, OnCallSchedule

class StaffMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffMember
        fields = '__all__'

class DutyRosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DutyRoster
        fields = '__all__'

class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = '__all__'

class OnCallScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnCallSchedule
        fields = '__all__'
