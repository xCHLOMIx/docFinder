from django.db import models
from users.models import MyUser

# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    choices = [
        ('General Practitioner' , 'General Practitioner'),
        ('Pediatrician' , 'Pediatrician'),
        ('Ophthalmologist' , 'Ophthalmologist'),
        ('Dermatologist' , 'Dermatologist'),
        ('Cardiologist' , 'Cardiologist'),
    ]
    specialty = models.CharField(max_length=50, choices=choices, default='General Practitioner')
    medical_license_number = models.CharField(max_length=10)
    practice_address = models.CharField(max_length=50)
    availability = models.CharField(max_length=80)

    def __str__(self):
        return self.user.first_name