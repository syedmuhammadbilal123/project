from django.shortcuts import render,redirect
from res.models import hotel_reservations
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.response import Response
from django.contrib import messages
from res.Serializers import ReservationSerializer

from . import Serializers
from . import models

# Create your views here.
def Home(request):
    """docstring for Home"""
    data = models.room_type.objects.all()
    return render(request,'base.html',{'data':data})

def login(request):

    return render(request,'vendor_login.html')

def login_Pressed(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(models.User.objects.filter(user_email=email)) > 0:
            redirect('res-home')
        # if len(models.vendor.objects.filter(vendor_email=email)) > 0:
        #     redirect('dash_vendor')
        # if len(models.admin.objects.filter(admin_email=email)) > 0:
        #     redirect('res-home')

    return render(request,'vendor_login.html')


def dashboard(request):
    return render(request,'dashboard.html')

def Index(request):
    b_data = models.vehicles.objects.all()
    return render(request,'index.html',{'data':b_data})


def add_reservation(request):
    if request.method == "POST":
        h_name = request.POST.get('hotel-name')
        c_in = request.POST.get('check-in')
        c_out = request.POST.get('check-out')
        d_arrival = request.POST.get('day-arrival')
        t_duration = request.POST.get('time-duration')
        t_amount = request.POST.get('total-amount')




        data = {'hotel_name':h_name,'check_in':c_in,'check_out':c_out,'day_arrival':d_arrival,'time_duration':t_duration,'total_amount':t_amount,'user_id':'2'}
        serial = ReservationSerializer(data=data)
        if serial.is_valid():
            try:
                serial.save()
                messages.success(request, 'Saved')
                return redirect('reservation-reservations')
            except:
                messages.error(request, 'Something wrong')
                return redirect('reservation-reservations')
        else:
            messages.error(request, 'Invalid Serializer')
            return redirect('reservation-reservations')
    else:
        return render(request,'sorry.html')

def add_booking(request):
    if request.method == "POST":
        v_name = request.POST.get('vehicles_name')
        v_type = request.POST.get('vehicles_type')
        data = {'vehicles_name':v_name,'vehicles_type':v_type,'vehicles_id':'1'}
        serial = Serializers.BookingSerializer(data=data)
        if serial.is_valid():
            try:
                serial.save()
                return redirect(request,'index.html')
            except:
                return redirect(request,'index.html')
        else:
            return redirect(request,'index.html')
