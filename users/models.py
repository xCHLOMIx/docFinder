from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        '''
        Creates and saves a User with the given email, date of
        birth and password.
        '''
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            is_patient = True,
            is_doctor = False
        )
        user.is_patient = True
        user.is_doctor = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        '''
        Creates and saves a superuser with the given email, date of
        birth and password.
        '''
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'is_patient', 'is_doctor']

    # def __str__(self):
    #     return self.email

    # def has_perm(self, perm, obj=None):
    #     'Does the user have a specific permission?'
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     'Does the user have permissions to view the app `app_label`?'
    #     # Simplest possible answer: Yes, always
    #     return True

    # @property
    # def is_staff(self):
    #     'Is the user a member of staff?'
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin