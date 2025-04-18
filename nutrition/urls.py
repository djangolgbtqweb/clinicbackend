from rest_framework.routers import DefaultRouter
from .views import (
    DietaryAssessmentViewSet,
    MealPlanViewSet,
    SupplementPrescriptionViewSet,
    ProgressMonitorViewSet
)

router = DefaultRouter()
router.register(r'dietary-assessments', DietaryAssessmentViewSet)
router.register(r'meal-plans', MealPlanViewSet)
router.register(r'supplements', SupplementPrescriptionViewSet)
router.register(r'progress', ProgressMonitorViewSet)

urlpatterns = router.urls
