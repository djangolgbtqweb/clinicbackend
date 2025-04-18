from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoticeViewSet, ShiftUpdateViewSet, AdminMessageViewSet

router = DefaultRouter()
router.register(r'notices', NoticeViewSet)
router.register(r'shift-updates', ShiftUpdateViewSet)
router.register(r'messages', AdminMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
