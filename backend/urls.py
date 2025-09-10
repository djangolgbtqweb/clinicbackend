# backend/backend/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patients.views import PatientViewSet, AppointmentViewSet, TestResultViewSet
from counseling.urls import router as counseling_router
from resource_management.views import WardViewSet, BedViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# DRF router for patients & appointments
router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'test-results', TestResultViewSet)
router.register(r'wards', WardViewSet)
router.register(r'beds', BedViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Core DRF endpoints
    path('api/', include(router.urls)),
    path('api/maternal-child-health/', include('maternal_child_health.urls')),
    path('api/nutrition/', include('nutrition.urls')),
    path('api/minor-theater/', include('minor_theater.urls')),
    path('api/pharmacy/', include('pharmacy.urls')),
    path('api/counseling/', include(counseling_router.urls)),
    path('api/laboratory/', include('laboratory.urls')),
    path('api/outpatient/', include('outpatient.urls')),
    path('api/staff/', include('staff.urls')),
    path('api/internal-communication/', include('internal_communication.urls')),
    path('api/emergency/', include('emergency.urls')),
    path('api/outreach/', include('outreach.urls')),
    path('api/chronic-disease-management/', include('chronic_disease_management.urls')),
    path('api/triage-vitals/', include('triage_vitals.urls')),
    path('api/billing-payments/', include('billing_payments.urls')),
    path('api/patient-portal/', include('patient_portal.urls')),
    path('api/inpatient/', include('inpatient.urls')),
   


    # **Resource Management must go here** so that
    # /api/resource-management/resource-equipment/ is routed correctly:
    path('api/resource-management/', include('resource_management.urls')),

    # Admin dashboard
    path('admin-dashboard/', include('admin_dashboard.urls')),
    
   # JWT auth endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]


