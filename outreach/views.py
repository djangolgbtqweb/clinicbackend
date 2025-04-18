from rest_framework import viewsets
from .models import CommunityHealthWorker, FieldVisit, MobileClinicDay
from .serializers import CommunityHealthWorkerSerializer, FieldVisitSerializer, MobileClinicDaySerializer

class CommunityHealthWorkerViewSet(viewsets.ModelViewSet):
    queryset = CommunityHealthWorker.objects.all()
    serializer_class = CommunityHealthWorkerSerializer

class FieldVisitViewSet(viewsets.ModelViewSet):
    queryset = FieldVisit.objects.all()
    serializer_class = FieldVisitSerializer

class MobileClinicDayViewSet(viewsets.ModelViewSet):
    queryset = MobileClinicDay.objects.all()
    serializer_class = MobileClinicDaySerializer

