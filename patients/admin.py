from django.contrib import admin
from .models import Patient, Appointment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'email', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('is_active', 'is_smoker', 'is_diabetic', 'is_pregnant')
    ordering = ('last_name', 'first_name')
    
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'appointment_date', 'appointment_status', 'created_at', 'updated_at')
    search_fields = ('patient__first_name', 'patient__last_name', 'appointment_date')
    list_filter = ('appointment_status',)
    ordering = ('appointment_date',)
