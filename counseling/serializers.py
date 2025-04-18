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
    class Meta:
        model = PrivateNote
        fields = '__all__'

class FollowUpReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUpReminder
        fields = '__all__'
