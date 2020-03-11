from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def backs(request):
    return render(request,'backs.html')

def dashboards(request):
    return render(request,'dashboards.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def train_schedule(request):
    return render(request,'train_schedule.html')

def airplane_schedule(request):
    return render(request,'airplane_schedule.html')
