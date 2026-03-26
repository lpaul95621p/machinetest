from rest_framework.viewsets import ModelViewSet
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.response import Response
class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        transformed_data = {
            "resource_type": data.get("resourceType"),
            "patient_id": data.get("id"),
            "active": data.get("active"),
            "gender": data.get("gender"),
            "birth_date": data.get("birthDate"),
            "name": data.get("name"),
            "identifier": data.get("identifier"),
            "telecom": data.get("telecom"),
        }

        serializer = self.get_serializer(data=transformed_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({
            "message": "Patient created successfully",
            "data": serializer.data
        })