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
    queryset = Equipment.objects.all().order_by('-id')
    serializer_class = EquipmentSerializer

class EquipmentBookingViewSet(viewsets.ModelViewSet):
    queryset = EquipmentBooking.objects.all()
    serializer_class = EquipmentBookingSerializer

class ResourceEquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.filter(used_in='resource').order_by('-id')  # use some field to filter
    serializer_class = EquipmentSerializer

    def perform_create(self, serializer):
        # Automatically tag new equipment as used in resource management
        serializer.save(used_in='resource')