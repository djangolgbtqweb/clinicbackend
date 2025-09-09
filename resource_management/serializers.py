from rest_framework import serializers
from .models import Room, RoomAssignment, Equipment, EquipmentBooking, Ward, Bed
from patients.serializers import PatientSerializer


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = ['id', 'ward', 'label', 'status', 'notes', 'created_at', 'patients']
        read_only_fields = ['id', 'created_at', 'label', 'ward']

class WardSerializer(serializers.ModelSerializer):
    beds = BedSerializer(many=True, read_only=True)
    patients = PatientSerializer(many=True, read_only=True)

    beds_count = serializers.SerializerMethodField()
    occupied_count = serializers.SerializerMethodField()
    available_count = serializers.SerializerMethodField()

    class Meta:
        model = Ward
        fields = [
            'id', 'name', 'ward_type', 'capacity', 'isolation', 'negative_pressure',
            'nursing_station', 'active', 'created_at',
            'beds', 'beds_count', 'occupied_count', 'available_count', 'patients'
        ]
        read_only_fields = ['id', 'created_at', 'beds', 'beds_count', 'occupied_count', 'available_count']

    def get_beds_count(self, obj):
        # If the value is already annotated, use it (fast)
        return getattr(obj, 'beds_count', obj.beds.count())

    def get_occupied_count(self, obj):
        return getattr(obj, 'occupied_count', obj.beds.filter(status='occupied').count())

    def get_available_count(self, obj):
        return getattr(obj, 'available_count', obj.beds.filter(status='available').count())


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
