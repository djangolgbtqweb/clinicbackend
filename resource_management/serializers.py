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

    def validate(self, data):
        room = data['room']
        date = data['date']
        slot = data['time_slot']

        # If updating an existing record, exclude it from the check
        qs = RoomAssignment.objects.filter(room=room, date=date, time_slot=slot)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError(
                f"Room {room} is already booked on {date} during {slot}."
            )
        return data

# resource_management/serializers.py

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'  # OR list actual model fields without 'quantity'

    def get_status(self, obj):
        # 👇 Return "Unavailable" only if condition is Broken
        return "Unavailable" if obj.condition == "Broken" else "Available"
    
class EquipmentBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentBooking
        fields = '__all__'
