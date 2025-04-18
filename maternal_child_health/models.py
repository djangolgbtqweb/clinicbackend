# backend/maternal_child_health/models.py
from django.db import models
from django.utils import timezone

class Patient(models.Model):
    """Assuming you have a Patient model defined already or you can use the existing Patient model from the `patients` app."""
    full_name = models.CharField(max_length=255)

class AntenatalPostnatalRecord(models.Model):
    """Stores antenatal/postnatal health records."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="health_records")
    record_date = models.DateTimeField(default=timezone.now)
    stage = models.CharField(max_length=50, choices=[('Antenatal', 'Antenatal'), ('Postnatal', 'Postnatal')])
    consultation_notes = models.TextField()
    health_status = models.CharField(max_length=100, choices=[('Normal', 'Normal'), ('At Risk', 'At Risk')])
    
    def __str__(self):
        return f"{self.patient.full_name} - {self.stage} Record"
class VaccinationRecord(models.Model):
    """Tracks vaccinations for maternal and child health."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="vaccinations")
    vaccine_name = models.CharField(max_length=255)
    vaccine_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Completed', 'Completed'), ('Pending', 'Pending')])
    
    def __str__(self):
        return f"{self.patient.full_name} - {self.vaccine_name} - {self.vaccine_date}"
class GrowthMonitoring(models.Model):
    """Tracks child growth milestones (height, weight, head circumference, etc.)."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="growth_monitoring")
    record_date = models.DateField(default=timezone.now)
    height = models.FloatField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")
    head_circumference = models.FloatField(help_text="Head circumference in cm")
    
    def __str__(self):
        return f"{self.patient.full_name} - {self.record_date}"
class FamilyPlanning(models.Model):
    """Tracks family planning services provided to patients."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="family_planning")
    service_type = models.CharField(max_length=100, choices=[('Contraceptive', 'Contraceptive'), ('Consultation', 'Consultation')])
    service_date = models.DateTimeField(default=timezone.now)
    details = models.TextField()
    
    def __str__(self):
        return f"{self.patient.full_name} - {self.service_type} - {self.service_date}"
