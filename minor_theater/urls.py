from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurgeryScheduleViewSet, OperationRecordViewSet, EquipmentTrackingViewSet, PostOpFollowUpViewSet

router = DefaultRouter()
router.register(r'surgeries', SurgeryScheduleViewSet)
router.register(r'operation-records', OperationRecordViewSet)
router.register(r'equipment', EquipmentTrackingViewSet)
router.register(r'post-op-followups', PostOpFollowUpViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
