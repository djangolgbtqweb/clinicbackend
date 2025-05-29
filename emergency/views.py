from rest_framework import viewsets
from .models import EmergencyCase, TriageLog, Referral, FirstAidInventory
from .serializers import EmergencyCaseSerializer, TriageLogSerializer, ReferralSerializer, FirstAidInventorySerializer

class EmergencyCaseViewSet(viewsets.ModelViewSet):
    queryset = EmergencyCase.objects.all()
    serializer_class = EmergencyCaseSerializer

from rest_framework.response import Response
from rest_framework import status

class TriageLogViewSet(viewsets.ModelViewSet):
    queryset = TriageLog.objects.all()
    serializer_class = TriageLogSerializer

    def create(self, request, *args, **kwargs):
        print('🚨 Incoming POST data:', request.data)
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print('❌ Serializer validation errors:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ReferralViewSet(viewsets.ModelViewSet):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer

class FirstAidInventoryViewSet(viewsets.ModelViewSet):
    queryset = FirstAidInventory.objects.all()
    serializer_class = FirstAidInventorySerializer

