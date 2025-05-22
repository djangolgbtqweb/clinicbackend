from django.db import models

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

    def __str__(self):
        return f"{self.name} ({self.room_type})"

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
