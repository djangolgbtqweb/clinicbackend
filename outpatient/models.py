# backend/outpatient/models.py
from django.db import models
from django.utils import timezone

from patients.models import Patient
from staff.models import StaffMember
class QueueEntry(models.Model):
    """Tracks patients waiting for outpatient services."""
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='queue_entries'
    )
    arrived_at = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = [
        ('waiting', 'Waiting'),
        ('in_consultation', 'In Consultation'),
        ('completed', 'Completed'),
        ('no_show', 'No Show'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')
    priority = models.PositiveIntegerField(
        default=0,
        help_text="Lower numbers = higher priority"
    )

    class Meta:
        ordering = ['status', 'priority', 'arrived_at']
        verbose_name = 'Queue Entry'
        verbose_name_plural = 'Queue Entries'

    def __str__(self):
        return f"{self.patient.full_name()} - {self.status}"


class ConsultationRecord(models.Model):
    """Stores details of a patient consultation."""
    queue_entry = models.OneToOneField(
        QueueEntry,
        on_delete=models.CASCADE,
        related_name='consultation'
    )
    consulted_at = models.DateTimeField(default=timezone.now)
    doctor_name = models.CharField(max_length=200)
    symptoms = models.TextField()
    diagnosis = models.TextField()
    prescriptions = models.TextField(
        blank=True,
        null=True,
        help_text="Medication or treatment plan."
    )
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-consulted_at']
        verbose_name = 'Consultation Record'
        verbose_name_plural = 'Consultation Records'

    def __str__(self):
        return f"Consultation for {self.queue_entry.patient.full_name()} on {self.consulted_at.date()}"


class Referral(models.Model):
    """Tracks referrals made during outpatient services."""
    consultation = models.ForeignKey(
        ConsultationRecord,
        on_delete=models.CASCADE,
        related_name='referrals'
    )
    referred_by = models.ForeignKey(
        StaffMember,
        on_delete=models.PROTECT,
        related_name='referrals_made',
        null=True,
        blank=True,
    )
    referred_to = models.CharField(
        max_length=200,
        help_text="Specialist or facility referred to."
    )
    reason = models.TextField(help_text="Reason for referral.")
    referred_at = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        ordering = ['-referred_at']
        verbose_name = 'Referral'
        verbose_name_plural = 'Referrals'

    def __str__(self):
        return f"Referral for {self.consultation.queue_entry.patient.full_name()} to {self.referred_to}"


# backend/outpatient/admin.py
from django.contrib import admin
from .models import QueueEntry, ConsultationRecord, Referral

@admin.register(QueueEntry)
class QueueEntryAdmin(admin.ModelAdmin):
    list_display = ('patient', 'status', 'priority', 'arrived_at')
    list_filter = ('status',)
    search_fields = ('patient__first_name', 'patient__last_name')
    ordering = ('status', 'priority', 'arrived_at')

@admin.register(ConsultationRecord)
class ConsultationRecordAdmin(admin.ModelAdmin):
    list_display = ('queue_entry', 'doctor_name', 'consulted_at')
    search_fields = (
        'queue_entry__patient__first_name',
        'queue_entry__patient__last_name',
        'doctor_name'
    )
    ordering = ('-consulted_at',)

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('consultation', 'referred_to', 'status', 'referred_at')
    list_filter = ('status',)
    search_fields = (
        'consultation__queue_entry__patient__first_name',
        'referred_to'
    )
    ordering = ('-referred_at',)


# backend/outpatient/serializers.py
from rest_framework import serializers
from .models import QueueEntry, ConsultationRecord, Referral

class QueueEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueEntry
        fields = '__all__'

class ConsultationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationRecord
        fields = '__all__'

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = '__all__'


# backend/outpatient/views.py
from rest_framework import viewsets
from .models import QueueEntry, ConsultationRecord, Referral
from .serializers import (
    QueueEntrySerializer,
    ConsultationRecordSerializer,
    ReferralSerializer
)

class QueueEntryViewSet(viewsets.ModelViewSet):
    queryset = QueueEntry.objects.all()
    serializer_class = QueueEntrySerializer

class ConsultationRecordViewSet(viewsets.ModelViewSet):
    queryset = ConsultationRecord.objects.all()
    serializer_class = ConsultationRecordSerializer

class ReferralViewSet(viewsets.ModelViewSet):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer
    



# backend/outpatient/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    QueueEntryViewSet,
    ConsultationRecordViewSet,
    ReferralViewSet
)

router = DefaultRouter()
router.register(r'queue', QueueEntryViewSet, basename='queueentry')
router.register(r'consultations', ConsultationRecordViewSet, basename='consultationrecord')
router.register(r'referrals', ReferralViewSet, basename='referral')

urlpatterns = [
    path('', include(router.urls)),
]


# backend/backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patients.views import PatientViewSet, AppointmentViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # DRF router for core API
    path('api/', include(router.urls)),
    # Additional app routes
    path('api/patients/', include('patients.urls')),
    path('api/outpatient/', include('outpatient.urls')),
]

