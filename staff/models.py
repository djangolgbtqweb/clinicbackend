import random
from django.db import models
from django.conf import settings

class StaffMember(models.Model):
    # link to the Django user account
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='staff_profile',
        null=True,
        blank=True
    )
    pin = models.CharField(
        max_length=4,
        unique=True,
        null=True,
        blank=True,
        help_text="4-digit numeric PIN for staff login (can be blank initially)"
    )
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        # Doctors
        ('Doctor - Cardiology', 'Doctor - Cardiology'),
        ('Doctor - Pediatrics', 'Doctor - Pediatrics'),
        ('Doctor - Gynecology', 'Doctor - Gynecology'),
        ('Doctor - General Surgery', 'Doctor - General Surgery'),
        ('Doctor - Internal Medicine', 'Doctor - Internal Medicine'),

        # Nurses
        ('Nurse - Registered', 'Nurse - Registered'),
        ('Nurse - Emergency', 'Nurse - Emergency'),
        ('Nurse - Pediatric', 'Nurse - Pediatric'),
        ('Nurse - Post-Operative Care', 'Nurse - Post-Operative Care'),
        ('Nurse - Chronic Care Management', 'Nurse - Chronic Care Management'),

        # Lab Technicians
        ('Lab Technician - Hematology', 'Lab Technician - Hematology'),
        ('Lab Technician - Microbiology', 'Lab Technician - Microbiology'),
        ('Lab Technician - Biochemistry', 'Lab Technician - Biochemistry'),
        ('Lab Technician - Molecular Diagnostics', 'Lab Technician - Molecular Diagnostics'),

        # Mental Health Counsellors
        ('Mental Health - Trauma Therapy', 'Mental Health - Trauma Therapy'),
        ('Mental Health - Adolescent Counseling', 'Mental Health - Adolescent Counseling'),
        ('Mental Health - CBT', 'Mental Health - CBT'),
        ('Mental Health - Stress & Anxiety', 'Mental Health - Stress & Anxiety'),

        # Dentists
        ('Dentist - Orthodontics', 'Dentist - Orthodontics'),
        ('Dentist - Cosmetic', 'Dentist - Cosmetic'),
        ('Dentist - Oral Surgery', 'Dentist - Oral Surgery'),
        ('Dentist - Pediatric', 'Dentist - Pediatric'),

        # Wellness Therapists
        ('Therapist - Physical Therapy', 'Therapist - Physical Therapy'),
        ('Therapist - Massage Therapy', 'Therapist - Massage Therapy'),
        ('Therapist - Rehabilitation', 'Therapist - Rehabilitation'),
        ('Therapist - Pain Management', 'Therapist - Pain Management'),

        # Nutritionists
        ('Nutritionist - Diabetic Diets', 'Nutritionist - Diabetic Diets'),
        ('Nutritionist - Pediatric Nutrition', 'Nutritionist - Pediatric Nutrition'),
        ('Nutritionist - Weight Management', 'Nutritionist - Weight Management'),
        ('Nutritionist - Clinical Meal Planning', 'Nutritionist - Clinical Meal Planning'),
    ]

    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    contact_info = models.TextField()
    profile_picture = models.ImageField(upload_to='staff_profiles/', blank=True, null=True)
    date_joined = models.DateField()
    
    def save(self, *args, **kwargs):
        if not self.pin:
            self.pin = self._generate_unique_pin()
        super().save(*args, **kwargs)

    def _generate_unique_pin(self):
        while True:
            pin = f"{random.randint(0, 9999):04d}"
            if not StaffMember.objects.filter(pin=pin).exists():
                return pin


    def __str__(self):
        return f"{self.name} ({self.role})"

class DutyRoster(models.Model):
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    date = models.DateField()
    shift_time = models.CharField(max_length=50, choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Weekend', 'Weekend'), ('Holidays', 'Holidays'), ('Evening', 'Evening'), ('Night', 'Night')])
    assigned = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.staff_member.name} - {self.shift_time} on {self.date}"

class LeaveRequest(models.Model):
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=50)
    reason = models.TextField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Pending'
    
    )
    rejection_reason = models.TextField(
        blank=True,
        null=True,
        help_text="If denied, why?"
    )
    def __str__(self):
        return f"Leave request from {self.staff_member.name} - {self.leave_type} ({self.status})"

class OnCallSchedule(models.Model):
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    date = models.DateField()
    is_on_call = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.staff_member.name} On-Call on {self.date}"

