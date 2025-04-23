from rest_framework import serializers
from .models import EmergencyCase, TriageLog, Referral, FirstAidInventory

# Basic EmergencyCase Serializer
class EmergencyCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyCase
        fields = '__all__'

# TriageLog with nested EmergencyCase
class TriageLogSerializer(serializers.ModelSerializer):
    emergency_case = EmergencyCaseSerializer(read_only=True)

    class Meta:
        model = TriageLog
        fields = '__all__'
        depth = 1

# Referral with nested EmergencyCase
class ReferralSerializer(serializers.ModelSerializer):
    emergency_case = EmergencyCaseSerializer(read_only=True)

    class Meta:
        model = Referral
        fields = '__all__'

# First Aid Inventory doesn't need nesting
class FirstAidInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstAidInventory
        fields = '__all__'
