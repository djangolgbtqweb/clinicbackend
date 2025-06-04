from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffMemberViewSet, DutyRosterViewSet, LeaveRequestViewSet, OnCallScheduleViewSet, StaffPinLoginView

router = DefaultRouter()
router.register(r'staff', StaffMemberViewSet)
router.register(r'duty-roster', DutyRosterViewSet)
router.register(r'leave-requests', LeaveRequestViewSet)
router.register(r'on-call-schedule', OnCallScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', StaffPinLoginView.as_view(), name='staff_pin_login'),
]
