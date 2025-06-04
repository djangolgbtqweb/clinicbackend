from rest_framework import serializers
from .models import StaffMember, DutyRoster, LeaveRequest, OnCallSchedule

class StaffMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffMember
        # include everything the front-end needs:
        fields = [
            'id',
            'name',
            'role',
            'contact_info',
            'profile_picture',
            'date_joined',
            'pin',               # ← newly added
        ]
        extra_kwargs = {
            # make it write‐optional so you can POST without explicitly providing pin
            'pin': {'required': False, 'allow_null': True},
        }

class DutyRosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DutyRoster
        fields = '__all__'
class LeaveRequestSerializer(serializers.ModelSerializer):
    # Use this to *write* the FK:
    staff_member = serializers.PrimaryKeyRelatedField(
        queryset=StaffMember.objects.all()
    )
    # And if you’d still like to return the nested object in responses:
    staff_member_detail = StaffMemberSerializer(
        source='staff_member',
        read_only=True
    )

    class Meta:
        model = LeaveRequest
        fields = [
          'id',
          'staff_member',        # the integer FK you post
          'staff_member_detail', # the nested read-only object,
          'start_date',
          'end_date',
          'leave_type',
          'reason',
          'status',
          'rejection_reason',
        ]

class OnCallScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnCallSchedule
        fields = '__all__'
