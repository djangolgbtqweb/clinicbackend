# inpatient/serializers.py
from rest_framework import serializers
from .models import Ward, Admission, Bed

class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = [
            'id', 'consultation', 'patient', 'ward', 'bed',
            'reason', 'status', 'admitted_at', 'created_at', 'admitted_by'
        ]
        read_only_fields = ['id', 'admitted_at', 'created_at', 'status', 'patient']
class WardCompactSerializer(serializers.ModelSerializer):
    beds_count = serializers.IntegerField(source='beds.count', read_only=True)
    available_count = serializers.SerializerMethodField()

    class Meta:
        model = Ward
        fields = ['id', 'name', 'capacity', 'beds_count', 'available_count']

    def get_available_count(self, obj):
        return obj.beds.filter(status='available').count()