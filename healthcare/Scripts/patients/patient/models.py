from django.db import models

class Patient(models.Model):
    resource_type = models.CharField(max_length=50)
    patient_id = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=True)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()

    name = models.JSONField()
    identifier = models.JSONField()
    telecom = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_id