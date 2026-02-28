from django.shortcuts import render
from .models import Member

def home(request):
    meme=Member.objects.all()
    return render(request,'home.html',{'sosa':meme})

def detail(request):
    return render(request,'details.html')
