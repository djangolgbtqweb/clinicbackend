from rest_framework.routers import DefaultRouter
from .views import (
    STIDiagnosisViewSet,
    STIMedicationViewSet,
    STIEducationMaterialViewSet,
    STIFollowUpViewSet,
)

router = DefaultRouter()
router.register(r'diagnoses', STIDiagnosisViewSet)
router.register(r'medications', STIMedicationViewSet)
router.register(r'education-materials', STIEducationMaterialViewSet)
router.register(r'followups', STIFollowUpViewSet)

urlpatterns = router.urls
