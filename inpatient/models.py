# inpatient/models.py
from django.db import models
from django.utils import timezone

from patients.models import Patient
from outpatient.models import ConsultationRecord
from resource_management.models import Ward, Bed


class Admission(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('admitted', 'Admitted'),
        ('discharged', 'Discharged'),
        ('canceled', 'Canceled'),
    ]

    consultation = models.OneToOneField(
        ConsultationRecord,
        on_delete=models.CASCADE,
        related_name='admission',
        help_text='Consultation that led to admission'
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='admissions'
    )
    ward = models.ForeignKey(
        Ward,
        on_delete=models.PROTECT,
        related_name='admissions'
    )
    bed = models.ForeignKey(
        Bed,
        on_delete=models.PROTECT,
        related_name='admissions',
        null=True,
        blank=True,
        help_text='Assigned bed (nullable until assigned)'
    )

    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admitted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    admitted_by = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        pt_name = getattr(self.patient, 'full_name', lambda: str(self.patient))()
        return f"Admission {self.id} - {pt_name} -> {self.ward.name}"

    def assign_bed(self, bed: Bed, save=True):
        """
        Assign a Bed to this admission. Caller should ensure transaction/locking.
        Marks bed occupied and links patient to bed/ward.
        """
        if bed.status != 'available':
            raise ValueError("Bed is not available")

        self.bed = bed
        self.status = 'admitted'
        self.admitted_at = timezone.now()

        # add patient to bed (assumes Bed has M2M 'patients') and mark bed occupied
        try:
            bed.patients.add(self.patient)
        except Exception:
            # if Bed.patients doesn't exist, ignore but still set status
            pass

        bed.status = 'occupied'
        bed.save()

        # add patient to ward's patients if ward has M2M
        try:
            self.ward.patients.add(self.patient)
        except Exception:
            pass

        if save:
            self.save()

    def free_bed(self, save=True):
        """
        Remove patient from bed and mark bed available if empty.
        """
        if not self.bed:
            return

        bed = self.bed
        try:
            bed.patients.remove(self.patient)
            if bed.patients.count() == 0:
                bed.status = 'available'
                bed.save()
        except Exception:
            # if bed.patients not present, simply set status
            bed.status = 'available'
            bed.save()

        self.bed = None
        self.status = 'discharged'
        self.save()
