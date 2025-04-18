from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiseaseViewSet, FollowUpViewSet

router = DefaultRouter()
router.register(r'diseases', DiseaseViewSet)
router.register(r'follow-ups', FollowUpViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
