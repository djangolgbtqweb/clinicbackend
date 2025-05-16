from django.db import models

# emergency/models.py

from django.db import models
from patients.models import Patient  # Adjust import if needed

class EmergencyCase(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='emergency_cases')
    
    description = models.TextField()
    
    severity = models.CharField(
        max_length=50,
        choices=[
            ('Critical', 'Critical'),
            ('Moderate', 'Moderate'),
            ('Mild', 'Mild'),
        ]
    )
    
    condition = models.CharField(
        max_length=50,
        choices=[
            ('Critical', 'Critical'),
            ('Stable', 'Stable'),
            ('Improving', 'Improving'),
            ('Worsening', 'Worsening'),
        ],
        default='Critical'
    )
    
    arrival_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.full_name()} — {self.severity}"


class TriageLog(models.Model):
    emergency_case = models.ForeignKey(EmergencyCase, on_delete=models.CASCADE)
    triage_notes   = models.TextField()
    triaged_by     = models.CharField(max_length=255)
    triage_time    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Triage by {self.triaged_by} for {self.emergency_case.patient_name}"

class Referral(models.Model):
    emergency_case = models.ForeignKey(EmergencyCase, on_delete=models.CASCADE)
    facility_name  = models.CharField(max_length=255)
    reason         = models.TextField()
    referred_on    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Referral of {self.emergency_case.patient_name} to {self.facility_name}"

class FirstAidInventory(models.Model):
    item_name    = models.CharField(max_length=255)
    quantity     = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name
