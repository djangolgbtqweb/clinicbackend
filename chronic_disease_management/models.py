from django.db import models
from patients.models import Patient

class Disease(models.Model):
    DISEASE_CHOICES = [
        ('Hypertension', 'Hypertension'),
        ('Diabetes Mellitus', 'Diabetes Mellitus'),
        ('Asthma', 'Asthma'),
        ('COPD', 'Chronic Obstructive Pulmonary Disease'),
        ('CKD', 'Chronic Kidney Disease'),
        ('CAD', 'Coronary Artery Disease'),
        ('Heart Failure', 'Heart Failure'),
        ('Hyperlipidemia', 'Hyperlipidemia'),
        ('Osteoarthritis', 'Osteoarthritis'),
        ('Rheumatoid Arthritis', 'Rheumatoid Arthritis'),
        ('Depression', 'Depression'),
        ('Anxiety Disorder', 'Anxiety Disorder'),
        ('Hypothyroidism', 'Hypothyroidism'),
        ('Hyperthyroidism', 'Hyperthyroidism'),
        ('GERD', 'Gastroesophageal Reflux Disease'),
        ('Epilepsy', 'Epilepsy'),
        ('Parkinson’s Disease', 'Parkinson’s Disease'),
        ('Dementia', 'Dementia'),
        ('HIV', 'HIV/AIDS'),
        ('Stroke', 'Stroke'),
        ('Obesity', 'Obesity'),
        ('Chronic Liver Disease', 'Chronic Liver Disease'),
        ('Anemia', 'Anemia'),
        # …add any others you commonly see
    ]

    STATUS_CHOICES = [
        ('Stable', 'Stable'),
        ('Unstable', 'Unstable'),
    ]

    patient         = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease_type    = models.CharField(max_length=50, choices=DISEASE_CHOICES)
    diagnosis_date  = models.DateField()
    treatment_plan  = models.TextField()
    status          = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        # Use first_name and last_name instead of name
        return f"{self.patient.first_name} {self.patient.last_name} – {self.disease_type}"

class FollowUp(models.Model):
    disease         = models.ForeignKey(Disease, on_delete=models.CASCADE)
    follow_up_date  = models.DateField()
    notes           = models.TextField()

    def __str__(self):
        # Use first_name and last_name instead of name
        return f"Follow-up for {self.disease.patient.first_name} {self.disease.patient.last_name} on {self.follow_up_date}"
