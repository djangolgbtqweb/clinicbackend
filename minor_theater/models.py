from django.db import models
from patients.models import Patient

class SurgerySchedule(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='surgeries')
    scheduled_date = models.DateTimeField()
    surgeon = models.CharField(max_length=255)
    procedure = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='scheduled')

    def __str__(self):
        return f"{self.patient.full_name} - {self.procedure} on {self.scheduled_date}"

class OperationRecord(models.Model):
    surgery = models.ForeignKey(SurgerySchedule, on_delete=models.CASCADE, related_name='operation_records')
    notes = models.TextField()
    outcome = models.CharField(max_length=255)
    performed_by = models.CharField(max_length=255)
    operation_date = models.DateTimeField()

    def __str__(self):
        return f"Operation record for {self.surgery.patient.full_name}"

class EquipmentTracking(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    last_checked = models.DateField()
    condition = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class PostOpFollowUp(models.Model):
    surgery = models.ForeignKey(SurgerySchedule, on_delete=models.CASCADE, related_name='follow_ups')
    follow_up_date = models.DateTimeField()
    notes = models.TextField()
    attended = models.BooleanField(default=False)

    def __str__(self):
        return f"Follow-up for {self.surgery.patient.full_name}"

