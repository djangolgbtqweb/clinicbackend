from rest_framework import viewsets
from .models import CounselingSession, HealthEducationLog, PrivateNote, FollowUpReminder
from .serializers import CounselingSessionSerializer, HealthEducationLogSerializer, PrivateNoteSerializer, FollowUpReminderSerializer

# ViewSet for CounselingSession
class CounselingSessionViewSet(viewsets.ModelViewSet):
    queryset = CounselingSession.objects.all()
    serializer_class = CounselingSessionSerializer

# ViewSet for HealthEducationLog
class HealthEducationLogViewSet(viewsets.ModelViewSet):
    queryset = HealthEducationLog.objects.all()
    serializer_class = HealthEducationLogSerializer

# ViewSet for PrivateNote
class PrivateNoteViewSet(viewsets.ModelViewSet):
    queryset = PrivateNote.objects.all()
    serializer_class = PrivateNoteSerializer

# ViewSet for FollowUpReminder
class FollowUpReminderViewSet(viewsets.ModelViewSet):
    queryset = FollowUpReminder.objects.all()
    serializer_class = FollowUpReminderSerializer
