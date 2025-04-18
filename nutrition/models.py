from django.db import models

class DietaryAssessment(models.Model):
    patient_name = models.CharField(max_length=100)
    date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return f"{self.patient_name} - {self.date}"

class MealPlan(models.Model):
    patient_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    plan_details = models.TextField()

    def __str__(self):
        return f"Meal Plan for {self.patient_name}"

class SupplementPrescription(models.Model):
    patient_name = models.CharField(max_length=100)
    supplement_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.patient_name} - {self.supplement_name}"

class ProgressMonitor(models.Model):
    patient_name = models.CharField(max_length=100)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bmi = models.DecimalField(max_digits=4, decimal_places=1)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient_name} - {self.date}"
