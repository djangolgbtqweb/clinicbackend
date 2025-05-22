from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from staff.models import StaffMember 
# Custom Manager to handle specific queries
class PatientManager(models.Manager):
    def active_patients(self):
        return self.filter(is_active=True)

    def inactive_patients(self):
        return self.filter(is_active=False)

class Patient(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    )
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
    )
    email = models.EmailField(unique=True)
    address = models.TextField()

    # Additional Patient Information
    is_active = models.BooleanField(
        default=True,
        help_text="Designates whether this patient is active."
    )
    allergies = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="List of known allergies (comma separated)."
    )
    blood_type = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        choices=[
            ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
            ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')
        ]
    )
    emergency_contact_name = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    emergency_contact_phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Emergency contact phone number must be in a valid format."
            )
        ],
        blank=True,
        null=True
    )
    is_smoker = models.BooleanField(default=False)
    is_diabetic = models.BooleanField(default=False)
    is_pregnant = models.BooleanField(default=False)

    # Medical History
    previous_conditions = models.TextField(
        blank=True,
        null=True,
        help_text="Describe any significant past medical history."
    )

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Manager to easily filter active and inactive patients
    objects = PatientManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} (DOB: {self.date_of_birth})"

    def full_name(self):
        """Returns the full name of the patient"""
        return f"{self.first_name} {self.last_name}"

    def age(self):
        """Calculates the current age of the patient based on date of birth"""
        from datetime import date
        return date.today().year - self.date_of_birth.year - (
            (date.today().month, date.today().day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = _("patient")
        verbose_name_plural = _("patients")

# Appointment Model
class Appointment(models.Model):
    # Link to the Patient
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    doctor = models.ForeignKey(  # Only link doctors from StaffMember
        StaffMember,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'role': 'Doctor'},  # This ensures only Doctors appear in admin/forms
        related_name='doctor_appointments'
    )

    purpose_of_visit = models.CharField(  # <-- NEW FIELD
        max_length=255,
        help_text="Brief reason or description for the appointment."
    )
    # Appointment Details
    appointment_date = models.DateTimeField()
    appointment_status = models.CharField(
        max_length=20,
        choices=[
            ('scheduled', 'Scheduled'),
            ('completed', 'Completed'),
            ('canceled', 'Canceled')
        ],
        default='scheduled',
    )

    # Additional Notes
    notes = models.TextField(blank=True, null=True)

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['appointment_date']
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"

    def __str__(self):
        return f"Appointment for {self.patient.full_name()} on {self.appointment_date}"

    def is_past_due(self):
        """Returns True if the appointment is in the past and hasn't been completed or canceled"""
        return self.appointment_date < timezone.now() and self.appointment_status not in ['completed', 'canceled']


class TestResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='test_results')
    test_name = models.CharField(max_length=255)
    result = models.TextField()
    date_conducted = models.DateField()
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.test_name} for {self.patient.full_name()} on {self.date_conducted}"
class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='medical_records'
    )
    record_type    = models.CharField(max_length=100)
    record_details = models.TextField()
    date_created   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Medical Record for "
            f"{self.patient.first_name} "
            f"{self.patient.last_name} "
            f"- {self.record_type}"
        )
