from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, RoomAssignmentViewSet, EquipmentViewSet, EquipmentBookingViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'room-assignments', RoomAssignmentViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'equipment-bookings', EquipmentBookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
