from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import patient_test_results
urlpatterns = [
    # GET  /api/patient-portal/medical-records/1/
    path(
        'medical-records/<int:patient_id>/',
        views.retrieve_medical_records,
        name='patient-medical-records'
    ),
    path('all-medical-records/', views.all_medical_records, name='all-medical-records'),

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
    path(
        'appointments/all/',
        views.all_appointments,
        name='patient-all-appointments'
    ),
    path('test-results/<int:patient_id>/', patient_test_results, name='patient-test-results'),
    
]