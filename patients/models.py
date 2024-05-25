from django.db import models
from users.models import MyUser

# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    insurance_company = models.CharField(max_length=50)
    insurance_policy_number = models.CharField(max_length=10)
    
    def __str__(self):
        return self.user.first_name