from django.db import models

class StaffMember(models.Model):
    ROLE_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Lab Technician', 'Lab Technician'),
        ('Admin', 'Admin'),
        # Add other roles here
    ]
    
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    contact_info = models.TextField()  # Can store phone, email, etc.
    profile_picture = models.ImageField(upload_to='staff_profiles/', blank=True, null=True)
    date_joined = models.DateField()
    
    def __str__(self):
        return f"{self.name} ({self.role})"

class DutyRoster(models.Model):
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    date = models.DateField()
    shift_time = models.CharField(max_length=50, choices=[('Morning', 'Morning'), ('Evening', 'Evening'), ('Night', 'Night')])
    assigned = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.staff_member.name} - {self.shift_time} on {self.date}"

class LeaveRequest(models.Model):
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=50)
    reason = models.TextField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Pending')
    
    def __str__(self):
        return f"Leave request from {self.staff_member.name} - {self.leave_type} ({self.status})"

class OnCallSchedule(models.Model):
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
    date = models.DateField()
    is_on_call = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.staff_member.name} On-Call on {self.date}"

