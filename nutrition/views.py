from rest_framework import viewsets
from .models import DietaryAssessment, MealPlan, SupplementPrescription, ProgressMonitor
from patients.models import Patient
from rest_framework.exceptions import NotFound
from .serializers import (
    DietaryAssessmentSerializer,
    MealPlanSerializer,
    SupplementPrescriptionSerializer,
    ProgressMonitorSerializer,
)

class DietaryAssessmentViewSet(viewsets.ModelViewSet):
    queryset = DietaryAssessment.objects.all()
    serializer_class = DietaryAssessmentSerializer

class MealPlanViewSet(viewsets.ModelViewSet):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer

class SupplementPrescriptionViewSet(viewsets.ModelViewSet):
    queryset = SupplementPrescription.objects.select_related('patient').all()
    serializer_class = SupplementPrescriptionSerializer

    def perform_create(self, serializer):
        patient_id = self.request.data.get('patient_id')

        if not patient_id:
            raise NotFound("Patient ID is required")

        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            raise NotFound("Patient not found")

        serializer.save(patient=patient)

class ProgressMonitorViewSet(viewsets.ModelViewSet):
    queryset = ProgressMonitor.objects.all()
    serializer_class = ProgressMonitorSerializer

    def perform_create(self, serializer):
        
        patient = Patient.objects.get(id=self.request.data.get("patient_id"))  
       
        serializer.save(patient=patient)


