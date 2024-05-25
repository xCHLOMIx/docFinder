from django.db import models
from patients.models import Patient
from doctors.models import Doctor

# Create your models here.

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=10, default='Pending...')
    feedback = models.TextField(null=True, default='Write Your Feedback here.')

    def __str__(self):
        return self.description