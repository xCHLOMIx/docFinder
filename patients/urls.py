from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signUpPage, name='patsignup'),
]
