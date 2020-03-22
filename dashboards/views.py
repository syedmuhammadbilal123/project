from django.shortcuts import render,redirect
from django.http import HttpResponse
from res import models


# Create your views here.


def backs(request):
    return render(request,'backs.html')

def dashboards(request):
    return render(request,'dashboards.html')

def login(request):
    return render(request,'vendor_login.html')

def register(request):
    return render(request,'register.html')

def train_schedule(request):
    return render(request,'train_schedule.html')

def airplane_schedule(request):
    return render(request,'airplane_schedule.html')

def login_Pressed(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(models.admin.objects.filter(admin_email=email)) > 0:
            redirect('admin-dashboard')
        # if len(models.vendor.objects.filter(vendor_email=email)) > 0:
        #     redirect('dash_vendor')
        # if len(models.admin.objects.filter(admin_email=email)) > 0:
        #     redirect('res-home')

    return render(request,'vendor_login.html')

def packages(request):
    events = models.event_places.objects.all()
    return render(request,"All_Events.html",{"data":events})

def all_Events(request):
    events = models.event_places.objects.all()
    return render(request,"Vendor_Events.html",{"data":events})