from django.db import models
from patients.models import Patient

class DietaryAssessment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return f"{self.patient.full_name} - {self.date}"

class MealPlan(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    plan_details = models.TextField()

    def __str__(self):
        return f"Meal Plan for {self.patient.full_name}"

class SupplementPrescription(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='supplements', null=True)
    supplement_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    start_date = models.DateField(null=True, blank=True)  # new
    end_date = models.DateField(null=True, blank=True)    # new

    def __str__(self):
        patient_name = self.patient.full_name() if self.patient else "No Patient"
        return f"{patient_name} - {self.supplement_name}"

class ProgressMonitor(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='progress_records',
    )
    date   = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bmi    = models.DecimalField(max_digits=4, decimal_places=1)
    notes  = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient.full_name if self.patient else 'Unknown'} – {self.date}"