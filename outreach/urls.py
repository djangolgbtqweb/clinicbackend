from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommunityHealthWorkerViewSet, FieldVisitViewSet, MobileClinicDayViewSet

router = DefaultRouter()
router.register(r'chws', CommunityHealthWorkerViewSet)
router.register(r'field-visits', FieldVisitViewSet)
router.register(r'mobile-clinics', MobileClinicDayViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
