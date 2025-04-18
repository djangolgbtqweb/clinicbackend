"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patients.views import PatientViewSet, AppointmentViewSet
from counseling.urls import router as counseling_router

# Initialize DRF router and register viewsets
router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # DRF browsable API via router
    path('api/', include(router.urls)),
    # Additional app-specific endpoints
    path('api/maternal-child-health/', include('maternal_child_health.urls')),
    path('api/nutrition/', include('nutrition.urls')),
    path('api/minor-theater/', include('minor_theater.urls')),
    path('api/pharmacy/', include('pharmacy.urls')),
    path('api/counseling/', include(counseling_router.urls)),
    path('api/laboratory/', include('laboratory.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/outpatient/', include('outpatient.urls')),
    path('api/stis/', include('stis.urls')),
    path('api/staff/', include('staff.urls')),
    path('api/internal-communication/', include('internal_communication.urls')),
    path('api/resource-management/', include('resource_management.urls')),
    path('api/emergency/', include('emergency.urls')),
    path('api/outreach/', include('outreach.urls')),
    path('api/chronic-disease-management/', include('chronic_disease_management.urls')),
    path('api/triage-vitals/', include('triage_vitals.urls')),
    path('api/billing-payments/', include('billing_payments.urls')),
    path('api/patient-portal/', include('patient_portal.urls')),
    path('admin-dashboard/', include('admin_dashboard.urls')), 
      






]


