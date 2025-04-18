from django.db import models
from patients.models import Patient  # Make sure this exists

class LabTest(models.Model):
    TEST_STATUS_CHOICES = [
        ('ordered', 'Ordered'),
        ('sample_collected', 'Sample Collected'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='lab_tests')
    test_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=TEST_STATUS_CHOICES, default='ordered')

    def __str__(self):
        return f"{self.test_name} for {self.patient.full_name}"


class SampleTracking(models.Model):
    lab_test = models.OneToOneField(LabTest, on_delete=models.CASCADE, related_name='sample')
    sample_collected_date = models.DateTimeField(null=True, blank=True)
    sample_received_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=100,
        choices=[
            ('pending', 'Pending'),
            ('collected', 'Collected'),
            ('in_lab', 'In Lab'),
            ('processed', 'Processed'),
        ],
        default='pending'
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Sample for {self.lab_test}"


class LabResult(models.Model):
    lab_test = models.OneToOneField(LabTest, on_delete=models.CASCADE, related_name='result')
    result_file = models.FileField(upload_to='lab_results/')
    result_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Result for {self.lab_test}"

