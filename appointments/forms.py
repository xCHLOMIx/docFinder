from django import forms
from django.forms import ModelForm
from .models import Appointment

class MakeAppointment(ModelForm):
    date = forms.DateField(widget = forms.SelectDateWidget())
    class Meta:
        model = Appointment
        fields = [
            'date',
            'description'
        ]
        widgets = {
            'description' : forms.Textarea(attrs={'placeholder' : 'Describe your problem'}),
            'date' : forms.DateInput(format='%d/%m/%Y'),
        }