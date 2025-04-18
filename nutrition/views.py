from rest_framework import viewsets
from .models import DietaryAssessment, MealPlan, SupplementPrescription, ProgressMonitor
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
    queryset = SupplementPrescription.objects.all()
    serializer_class = SupplementPrescriptionSerializer

class ProgressMonitorViewSet(viewsets.ModelViewSet):
    queryset = ProgressMonitor.objects.all()
    serializer_class = ProgressMonitorSerializer

