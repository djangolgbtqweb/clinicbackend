# patients/models.py

from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()  # Date of birth
    gender = models.CharField(max_length=10)  # M/F/Other
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class TestResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='test_results')
    test_name = models.CharField(max_length=255)
    result = models.TextField()
    date_of_test = models.DateField()
    technician_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Test Result for {self.patient.first_name} {self.patient.last_name} - {self.test_name}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    doctor_name = models.CharField(max_length=255)
    purpose_of_visit = models.CharField(max_length=255)

    def __str__(self):
        return f"Appointment for {self.patient.first_name} {self.patient.last_name} with {self.doctor_name}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    record_type = models.CharField(max_length=100)  # e.g., Diagnosis, Prescription, etc.
    record_details = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Medical Record for {self.patient.first_name} {self.patient.last_name} - {self.record_type}"
