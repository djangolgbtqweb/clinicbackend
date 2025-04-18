from rest_framework import viewsets
from .models import Notice, ShiftUpdate, AdminMessage
from .serializers import NoticeSerializer, ShiftUpdateSerializer, AdminMessageSerializer

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all().order_by('-posted_at')
    serializer_class = NoticeSerializer

class ShiftUpdateViewSet(viewsets.ModelViewSet):
    queryset = ShiftUpdate.objects.all().order_by('-timestamp')
    serializer_class = ShiftUpdateSerializer

class AdminMessageViewSet(viewsets.ModelViewSet):
    queryset = AdminMessage.objects.all().order_by('-sent_at')
    serializer_class = AdminMessageSerializer

