from django.db import models
from patients.models import Patient

class Disease(models.Model):
    DISEASE_CHOICES = [
        ('Hypertension', 'Hypertension'),
        ('Diabetes', 'Diabetes'),
        ('Asthma', 'Asthma'),
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease_type = models.CharField(max_length=50, choices=DISEASE_CHOICES)
    diagnosis_date = models.DateField()
    treatment_plan = models.TextField()
    status = models.CharField(max_length=50, choices=[('Stable', 'Stable'), ('Unstable', 'Unstable')])

    def __str__(self):
        return f"{self.patient.name} - {self.disease_type}"

class FollowUp(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    follow_up_date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return f"Follow-up for {self.disease.patient.name} on {self.follow_up_date}"

