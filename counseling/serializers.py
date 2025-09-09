from rest_framework import serializers
from .models import CounselingSession, HealthEducationLog, PrivateNote, FollowUpReminder

class CounselingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounselingSession
        fields = '__all__'

class HealthEducationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthEducationLog
        fields = '__all__'

class PrivateNoteSerializer(serializers.ModelSerializer):
    # no need to declare counselor_pin explicitly—
    # ModelSerializer will pick it up automatically
    class Meta:
        model = PrivateNote
        fields = [
            'id',
            'session',
            'counselor',
            'counselor_pin',   # now writable & readable
            'note',
            'created_at',
        ]
        extra_kwargs = {
            'counselor_pin': {'required': True},
        }

class FollowUpReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUpReminder
        fields = '__all__'
