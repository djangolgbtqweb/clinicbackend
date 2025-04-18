from rest_framework import serializers
from .models import Notice, ShiftUpdate, AdminMessage

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

class ShiftUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftUpdate
        fields = '__all__'

class AdminMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminMessage
        fields = '__all__'
