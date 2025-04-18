from rest_framework import viewsets
from .models import Room, RoomAssignment, Equipment, EquipmentBooking
from .serializers import RoomSerializer, RoomAssignmentSerializer, EquipmentSerializer, EquipmentBookingSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomAssignmentViewSet(viewsets.ModelViewSet):
    queryset = RoomAssignment.objects.all()
    serializer_class = RoomAssignmentSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class EquipmentBookingViewSet(viewsets.ModelViewSet):
    queryset = EquipmentBooking.objects.all()
    serializer_class = EquipmentBookingSerializer
