from rest_framework import serializers
from datetime import date
import re
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'

    # ✅ Age validation
    def validate_birth_date(self, value):
        today = date.today()
        age = today.year - value.year - (
            (today.month, today.day) < (value.month, value.day)
        )

        if age < 18:
            raise serializers.ValidationError("Patient must be at least 18 years old.")
        return value

    # ✅ SSN format validation
    def validate_identifier(self, value):
        for item in value:
            if item.get("system") == "http://hl7.org/fhir/sid/us-ssn":
                ssn = item.get("value", "")
                if not re.match(r"^\d{3}-\d{2}-\d{4}$", ssn):
                    raise serializers.ValidationError("SSN must be in XXX-XX-XXXX format")
        return value

    # ✅ Mask SSN in response
    def to_representation(self, instance):
        data = super().to_representation(instance)

        identifiers = data.get("identifier", [])
        for item in identifiers:
            if item.get("system") == "http://hl7.org/fhir/sid/us-ssn":
                ssn = item.get("value", "")
                if len(ssn) >= 4:
                    item["value"] = "***-**-" + ssn[-4:]

        data["identifier"] = identifiers
        return data