from django.db import models

class STIDiagnosis(models.Model):
    patient_id = models.IntegerField()
    diagnosis_date = models.DateField()
    sti_type = models.CharField(max_length=100)
    symptoms = models.TextField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.sti_type} - {self.patient_id}"

class STIMedication(models.Model):
    diagnosis = models.ForeignKey(STIDiagnosis, on_delete=models.CASCADE, related_name='medications')
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.medication_name

class STIEducationMaterial(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class STIFollowUp(models.Model):
    diagnosis = models.ForeignKey(STIDiagnosis, on_delete=models.CASCADE, related_name='followups')
    follow_up_date = models.DateField()
    status = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Follow-up for {self.diagnosis}"

