from django.db import models
from django.utils import timezone

class Medication(models.Model):
    """Represents a medication in the pharmacy inventory."""
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
    @property
    def total_price(self):
        """Calculate the total price based on quantity and price per unit."""
        return self.quantity * self.price_per_unit

class Prescription(models.Model):
    """Stores prescription details for medications provided to patients."""
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='prescriptions')
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name='prescriptions')
    dose = models.CharField(max_length=255)
    prescribed_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Prescription for {self.patient.full_name} - {self.medication.name}"

class DispensingHistory(models.Model):
    """Tracks dispensing of medications to patients."""
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='dispensing_history')
    dispense_date = models.DateTimeField(default=timezone.now)
    quantity_dispensed = models.PositiveIntegerField()

    def __str__(self):
        return f"Dispensed {self.quantity_dispensed} units of {self.prescription.medication.name} to {self.prescription.patient.full_name}"

class RestockingAlert(models.Model):
    """Triggers an alert for restocking when medication quantity is low."""
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name='restocking_alerts')
    threshold_quantity = models.PositiveIntegerField(default=10)
    alert_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Restocking alert for {self.medication.name} at {self.threshold_quantity} units"
