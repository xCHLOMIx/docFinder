from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import *

# Create your views here.

def signUpPage(request):
    form = UserForm()
    doctor_form = DoctorForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        doctor_form = DoctorForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = False
            user.is_doctor = True
            user.set_password(request.POST['password'])
            user.save()

            if doctor_form.is_valid():
                doctor = doctor_form.save(commit=False)
                doctor.user = user
                doctor.save()
                return redirect('signin')
    return render(request, 'doctors/signup.html', {'user' : form, 'doctor' : doctor_form})