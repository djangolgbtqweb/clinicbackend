# resource_management/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RoomViewSet,
    RoomAssignmentViewSet,
    EquipmentViewSet,
    EquipmentBookingViewSet,
    ResourceEquipmentViewSet,
)

# Main router for the “minor theater” style endpoints
main_router = DefaultRouter()
main_router.register(r'rooms', RoomViewSet)
main_router.register(r'room-assignments', RoomAssignmentViewSet)
main_router.register(r'equipment', EquipmentViewSet)
main_router.register(r'equipment-bookings', EquipmentBookingViewSet)

# Separate router for resource-management’s equipment
resource_router = DefaultRouter()
resource_router.register(
    r'resource-equipment',
    ResourceEquipmentViewSet,
    basename='resource-equipment'
)

urlpatterns = [
    # These all mount under whatever prefix your project uses.
    # If your project’s urls.py has:
    #     path('api/resource-management/', include('resource_management.urls'))
    # then these will live at:
    #   /api/resource-management/rooms/
    #   /api/resource-management/room-assignments/
    #   /api/resource-management/equipment/
    #   /api/resource-management/equipment-bookings/
    #   /api/resource-management/resource-equipment/
    path('', include(main_router.urls)),
    path('', include(resource_router.urls)),
]


