from patient.viewsets import PatientViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('patient-intake',PatientViewSet)