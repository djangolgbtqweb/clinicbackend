from django.db import models
from patients.models import Patient

class Triage(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    triage_notes = models.TextField()

    def __str__(self):
        return f"Triage for {self.patient.name} on {self.date}"

class VitalSign(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    blood_pressure = models.CharField(max_length=20)
    heart_rate = models.IntegerField()
    temperature = models.FloatField()

    def __str__(self):
        return f"Vitals for {self.patient.name} on {self.date}"
