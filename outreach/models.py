from django.db import models

class CommunityHealthWorker(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class FieldVisit(models.Model):
    chw = models.ForeignKey(CommunityHealthWorker, on_delete=models.CASCADE)
    date = models.DateField()
    location = models.CharField(max_length=255)
    purpose = models.TextField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.chw.name} - {self.date} at {self.location}"

class MobileClinicDay(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=255)
    services_provided = models.TextField()
    outcome_summary = models.TextField()

    def __str__(self):
        return f"Mobile Clinic - {self.date} - {self.location}"
