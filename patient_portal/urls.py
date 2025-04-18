from django.urls import path
from . import views

urlpatterns = [
    # GET  /api/patient-portal/medical-records/1/
    path(
        'medical-records/<int:patient_id>/',
        views.retrieve_medical_records,
        name='patient-medical-records'
    ),

    # GET  /api/patient-portal/test-results/1/
    path(
        'test-results/<int:patient_id>/',
        views.retrieve_test_results,
        name='patient-test-results'
    ),

    # GET  /api/patient-portal/appointments/1/
    path(
        'appointments/<int:patient_id>/',
        views.retrieve_appointments,
        name='patient-appointments'
    ),

    # POST /api/patient-portal/schedule-appointment/
    path(
        'schedule-appointment/',
        views.schedule_appointment,
        name='patient-schedule-appointment'
    ),
]

