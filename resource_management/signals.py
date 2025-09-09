# resource_management/signals.py
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Patient, Bed

@receiver(pre_delete, sender=Patient)
def free_bed_on_patient_delete(sender, instance, **kwargs):
    beds = Bed.objects.filter(patients=instance)
    for bed in beds:
        bed.patients.remove(instance)
        if bed.patients.count() == 0:
            bed.status = 'available'
            bed.save()
