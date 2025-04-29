from rest_framework import serializers
from .models import Notice, ShiftUpdate, AdminMessage

# internal_communication/serializers.py

class NoticeSerializer(serializers.ModelSerializer):
    posted_by_name = serializers.CharField(source='posted_by.name', read_only=True)

    class Meta:
        model  = Notice
        fields = ['id','reference','title','content','posted_by','posted_by_name','posted_at']


class ShiftUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftUpdate
        fields = '__all__'

class AdminMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminMessage
        fields = '__all__'
