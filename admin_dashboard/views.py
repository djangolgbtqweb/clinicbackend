from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from patients.models import Patient, Appointment
from staff.models import Staff  # If you have a staff model

# Only allow logged-in users who are staff
@user_passes_test(lambda u: u.is_staff)
@login_required
def dashboard_home(request):
    total_patients = Patient.objects.count()
    total_appointments = Appointment.objects.count()
    staff_on_duty = Staff.objects.filter(status='On Duty').count() if hasattr(Staff, 'status') else None

    context = {
        'total_patients': total_patients,
        'total_appointments': total_appointments,
        'staff_on_duty': staff_on_duty,
    }

    return render(request, 'admin_dashboard/dashboard.html', context)
