from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CounselingSessionViewSet, HealthEducationLogViewSet, PrivateNoteViewSet, FollowUpReminderViewSet

router = DefaultRouter()
router.register(r'counseling-sessions', CounselingSessionViewSet)
router.register(r'health-education-logs', HealthEducationLogViewSet)
router.register(r'private-notes', PrivateNoteViewSet)
router.register(r'follow-up-reminders', FollowUpReminderViewSet)

urlpatterns = [
    path('api/counseling/', include(router.urls)),  # Include the router URLs under 'api/counseling/'
]
