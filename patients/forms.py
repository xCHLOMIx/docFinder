from django.forms import ModelForm, widgets
from django import forms 
from .models import Patient
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

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = [
            'age',
            'address',
            'insurance_company',
            'insurance_policy_number'
        ]
        widgets = {
            'age': forms.TextInput(attrs={'required': '', 'placeholder' : 'Age'}),
            'address': forms.TextInput(attrs={'required': '', 'placeholder' : 'Address eg: Gasabo', 'type' : 'text'}),
            'insurance_company': forms.TextInput(attrs={'required': '', 'placeholder' : 'Insurance Company', 'type' : 'text'}),
            'insurance_policy_number': forms.TextInput(attrs={'required': '', 'placeholder' : 'Insurance Policy Number', 'type' : 'number'})
        }