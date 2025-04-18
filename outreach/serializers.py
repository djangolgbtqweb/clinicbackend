from rest_framework import serializers
from .models import CommunityHealthWorker, FieldVisit, MobileClinicDay

class CommunityHealthWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityHealthWorker
        fields = '__all__'

class FieldVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldVisit
        fields = '__all__'

class MobileClinicDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileClinicDay
        fields = '__all__'
