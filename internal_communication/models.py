from django.db import models
from staff.models import StaffMember

class Notice(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    posted_by = models.ForeignKey(StaffMember, on_delete=models.SET_NULL, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ShiftUpdate(models.Model):
    message = models.TextField()
    updated_by = models.ForeignKey(StaffMember, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shift update by {self.updated_by} at {self.timestamp}"

class AdminMessage(models.Model):
    sender = models.ForeignKey(StaffMember, on_delete=models.SET_NULL, null=True, related_name='sent_messages')
    recipient = models.ForeignKey(StaffMember, on_delete=models.SET_NULL, null=True, related_name='received_messages')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.recipient}"

