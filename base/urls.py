from django.urls import path
from .views import *

urlpatterns = [
    path('doc-home/', doctorPage, name='doctor'),
    path('pat-home/', patientPage, name='patient'),
    path('signin/', signInPage, name='signin'),
    path('book/<str:doctor>/', bookAppointment, name='book'),
    path('book/<str:doctor>/', bookAppointment, name='that'),
    path('signout/', signout, name='signout'),
    path('', HomePage.as_view(), name='home')
]
