# backend/pharmacy/views.py
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Medication, Prescription, DispensingHistory, RestockingAlert
from .serializers import MedicationSerializer, PrescriptionSerializer, DispensingHistorySerializer, RestockingAlertSerializer

# ViewSet for Medication
class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

# ViewSet for Prescription
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

# ViewSet for DispensingHistory
class DispensingHistoryViewSet(viewsets.ModelViewSet):
    queryset = DispensingHistory.objects.all()
    serializer_class = DispensingHistorySerializer

# ViewSet for RestockingAlert
class RestockingAlertViewSet(viewsets.ModelViewSet):
    queryset = RestockingAlert.objects.all()
    serializer_class = RestockingAlertSerializer

# Custom APIView for getting the total cost of a medication
class TotalCostView(APIView):
    """Get the total cost for a specific medication by its id."""
    
    def get(self, request, pk):
        try:
            medication = Medication.objects.get(pk=pk)
            total_cost = medication.quantity * medication.price_per_unit
            return Response({'total_cost': total_cost}, status=status.HTTP_200_OK)
        except Medication.DoesNotExist:
            return Response({'detail': 'Medication not found'}, status=status.HTTP_404_NOT_FOUND)


