from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

# Import your Patient model — adjust the import path as needed
from patients.models import Patient  


class Room(models.Model):
    ROOM_TYPES = [
        ('Consultation', 'Consultation'),
        ('Lab', 'Lab'),
        ('Theater', 'Theater'),
        ('Inpatient', 'Inpatient'),
    ]
    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    is_occupied = models.BooleanField(default=False)
    patients = models.ManyToManyField(Patient, blank=True, related_name='rooms')

    def __str__(self):
        return f"{self.name} ({self.room_type})"


class Ward(models.Model):
    WARD_TYPES = [
        ('ICU', 'ICU'),
        ('HDU', 'HDU / Step-down'),
        ('GENERAL', 'General / Medical'),
        ('SURGICAL', 'Surgical'),
        ('MATERNITY', 'Maternity'),
        ('NICU', 'NICU'),
        ('PEDIATRIC', 'Pediatric'),
        ('ISOLATION', 'Isolation'),
        ('PSYCHIATRIC', 'Psychiatric'),
        ('BURN', 'Burn Unit'),
        ('PACU', 'PACU / Recovery'),
        ('CONSULT', 'Consultation / Clinic'),
        ('PROCEDURE', 'Procedure Room'),
        ('TRIAGE', 'Triage / Observation'),
        ('DIALYSIS', 'Dialysis Station'),
        ('IMAGING', 'Imaging / Radiology'),
        ('PHARMACY', 'Pharmacy Area'),
        ('SUPPORT', 'Support / Admin'),
    ]

    name = models.CharField(max_length=200, help_text="e.g. General Ward A")
    ward_type = models.CharField(max_length=30, choices=WARD_TYPES)
    capacity = models.PositiveIntegerField(default=0, help_text="Number of beds (0 for non-bed areas)")
    isolation = models.BooleanField(default=False)
    negative_pressure = models.BooleanField(default=False)
    nursing_station = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)
    patients = models.ManyToManyField(Patient, blank=True, related_name='wards')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ward_type', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_ward_type_display()})"

    @property
    def beds_count(self):
        return self.beds.count()

    @property
    def occupied_count(self):
        return self.beds.filter(status='occupied').count()

    @property
    def available_count(self):
        return self.beds.filter(status='available').count()


class Bed(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('reserved', 'Reserved'),
        ('cleaning', 'Cleaning'),
        ('maintenance', 'Maintenance'),
    ]

    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='beds')
    label = models.CharField(max_length=100, help_text="e.g. General-01 or Bed 01")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    notes = models.TextField(blank=True, null=True)
    patients = models.ManyToManyField(Patient, blank=True, related_name='beds')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('ward', 'label')
        ordering = ['ward', 'label']

    def __str__(self):
        return f"{self.ward.name} — {self.label} ({self.get_status_display()})"


@receiver(post_save, sender=Ward)
def ensure_beds_for_ward(sender, instance: Ward, created, **kwargs):
    existing = instance.beds.count()
    target = instance.capacity or 0

    if target <= existing:
        return

    existing_labels = set(b.label for b in instance.beds.all())
    to_create = []
    i = 1
    while len(to_create) + existing < target:
        label = f"{instance.name}-{i:02d}"
        if label not in existing_labels:
            to_create.append(Bed(ward=instance, label=label))
        i += 1
    if to_create:
        Bed.objects.bulk_create(to_create)
class RoomAssignment(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=255)
    patient_name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    time_slot = models.CharField(max_length=100)  # "10:00 - 11:00"

    class Meta:
        unique_together = ('room', 'date', 'time_slot')
        ordering = ['date', 'time_slot']

    def __str__(self):
        return f"{self.room} → {self.staff_name} @ {self.time_slot} on {self.date}"
class Equipment(models.Model):
    USED_IN_CHOICES = [
        ('minor', 'Minor Theater'),
        ('resource', 'Resource Management'),
    ]
    CONDITION_CHOICES = [
        ('Good', 'Good'),
        ('Needs Repair', 'Needs Repair'),
        ('Broken', 'Broken'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    used_in = models.CharField(max_length=50, choices=USED_IN_CHOICES, default='resource')
    quantity = models.PositiveIntegerField(default=1) 
    
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES, default='Good')
    last_checked = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.get_used_in_display()})"


class EquipmentBooking(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    booked_by = models.CharField(max_length=255)
    date = models.DateField()
    time_slot = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.equipment.name} booked by {self.booked_by} at {self.time_slot} on {self.date}"
