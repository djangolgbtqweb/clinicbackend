from django.db import models
from patients.models import Patient  # Assuming you have a Patient model in the patients app

class CounselingSession(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='counseling_sessions')
    counselor = models.CharField(max_length=255)  # You can use a related user model if you have counselors defined
    session_date = models.DateTimeField()
    session_notes = models.TextField(blank=True)
    session_type = models.CharField(max_length=100, choices=[('mental_health', 'Mental Health'), ('health_education', 'Health Education')])

    def __str__(self):
        return f"Session with {self.patient.full_name} on {self.session_date}"

class HealthEducationLog(models.Model):
    session = models.ForeignKey(CounselingSession, on_delete=models.CASCADE, related_name='health_education_logs')
    topic_covered = models.CharField(max_length=255)
    log_notes = models.TextField(blank=True)
    follow_up_required = models.BooleanField(default=False)
    follow_up_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Education log for {self.session.patient.full_name}"

class PrivateNote(models.Model):
    session = models.ForeignKey(CounselingSession, on_delete=models.CASCADE, related_name='private_notes')
    counselor = models.CharField(max_length=255)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Private note for {self.session.patient.full_name}"

class FollowUpReminder(models.Model):
    counseling_session = models.ForeignKey(CounselingSession, on_delete=models.CASCADE, related_name='follow_up_reminders')
    reminder_date = models.DateTimeField()
    reminder_notes = models.TextField(blank=True)

    def __str__(self):
        return f"Follow-up reminder for {self.counseling_session.patient.full_name}"
