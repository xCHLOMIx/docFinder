from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import *

def signUpPage(request):
    form = UserForm()
    patient_form = PatientForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        patient_form = PatientForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.set_password(request.POST['password'])
            user.save()

            if patient_form.is_valid():
                patient = patient_form.save(commit=False)
                patient.user = user
                patient.save()
                return redirect('signin')
    return render(request, 'patients/signup.html', {'user' : form, 'patient' : patient_form})