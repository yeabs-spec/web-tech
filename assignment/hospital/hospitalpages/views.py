from django.shortcuts import render
from .models import Hospital

def home(request):
    hospital=Hospital.objects.all()
    return render(request,'home.html',{'hospital':hospital})

def details(request):
    return render(request,'details.html')


