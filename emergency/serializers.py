from rest_framework import serializers
from .models import EmergencyCase, TriageLog, Referral, FirstAidInventory

class EmergencyCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyCase
        fields = '__all__'

class TriageLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TriageLog
        fields = '__all__'

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = '__all__'

class FirstAidInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstAidInventory
        fields = '__all__'
