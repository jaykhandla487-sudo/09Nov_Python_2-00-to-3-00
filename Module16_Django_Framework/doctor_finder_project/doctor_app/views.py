from django.shortcuts import render
from .models import Doctor

def home(request):

    doctors = Doctor.objects.all()

    return render(request, 'index.html', {'doctors': doctors})