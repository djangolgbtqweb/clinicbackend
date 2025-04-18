from rest_framework import serializers
from .models import Room, RoomAssignment, Equipment, EquipmentBooking

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class RoomAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomAssignment
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class EquipmentBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentBooking
        fields = '__all__'
