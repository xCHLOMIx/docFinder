from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import SignInForm
from appointments.forms import MakeAppointment
from django.contrib import messages
from doctors.models import Doctor
from appointments.models import Appointment
from patients.models import Patient
from django.views.generic import TemplateView

# Create your views here.
@login_required(login_url='signin')
def doctorPage(request):
    appointment = Appointment.objects.all()

    return render(request, 'doc-home.html', {'appointments': appointment})


@login_required(login_url='signin')
def approve(request, pk):
    appointment = Appointment.objects.all()
    
    return render(request, 'approve.html')
@login_required(login_url='signin')
def doctorPage(request):
    appointment = Appointment.objects.all()

    return render(request, 'doc-home.html', {'appointments': appointment})

@login_required(login_url='signin')
def patientPage(request):
    doctor = Doctor.objects.all()
    appointments = Appointment.objects.all()

    return render(request, 'pat-home.html', {'doctors': doctor, 'appointments' : appointments})

@login_required(login_url='signin')
def bookAppointment(request, doctor):
    doctor = Doctor.objects.get(id = doctor)
    form = MakeAppointment()

    print(request.user)

    patient = Patient.objects.get(user = request.user)

    if request.method == 'POST':
        form = MakeAppointment(request.POST)

        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.doctor = doctor
            appointment.save()

            return redirect('patient')

    return render(request, 'book.html', {'doctor' : doctor, 'forms' : form})

# Create your views here.

def signInPage(request):
    form = SignInForm()

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email = email, password = password)
        if user is not None:
            login(request, user)
            if user.is_patient == True and user.is_doctor == False:
                return redirect('patient')
            elif user.is_doctor == True and user.is_patient == False:
                return redirect('doctor')
            else:
                messages.error(request, 'Invalid email or password!')
    return render(request, 'signin.html', {'form' : form})

def signout(request):
    logout(request)
    return redirect('signin')

class HomePage(TemplateView):
    template_name = 'index.html'