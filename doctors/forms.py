from django.forms import ModelForm, widgets
from django import forms 
from .models import Doctor
from users.models import MyUser


class UserForm(ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'password'
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'required': '', 'placeholder' : 'example@gmail.com'}),
            'first_name': forms.TextInput(attrs={'required': '', 'placeholder' : 'First Name', 'type' : 'text'}),
            'last_name': forms.TextInput(attrs={'required': '', 'placeholder' : 'Last Name', 'type' : 'text'}),
            'password': forms.PasswordInput(attrs={'required': '', 'placeholder' : 'Password'})
        }

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'specialty',
            'medical_license_number',
            'practice_address',
            'availability'
        ]
        widgets = {
            'practice_address': forms.TextInput(attrs={'required': '', 'placeholder' : 'Workplace'}),
            'medical_license_number': forms.TextInput(attrs={'required': '', 'placeholder' : 'Medical License Number'}),
            'availability': forms.TextInput(attrs={'required': '', 'placeholder' : 'Availability. eg: Weekdays 9:00 - 5:00', 'type' : 'text'})
        }

class SignInForm(ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'email',
            'password',
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'required': '', 'placeholder' : 'example@gmail.com'}),
            'password': forms.PasswordInput(attrs={'required': '', 'placeholder' : 'Password'})
        }