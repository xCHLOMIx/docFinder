from django.forms import ModelForm, widgets
from django import forms 
from users.models import MyUser

class SignInForm(ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'email',
            'password'
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'required': '', 'placeholder' : 'example@gmail.com'}),
            'password': forms.PasswordInput(attrs={'required': '', 'placeholder' : 'Password'})
        }