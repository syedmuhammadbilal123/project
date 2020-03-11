from django.shortcuts import render,redirect

from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.response import Response

from . import Serializers
from . import models

# Create your views here.
def Home(request):
    """docstring for Home"""
    n_data = models.hotel_reservations.objects.all()
    return render(request,'base.html',{'data':n_data})

def Index(request):
    b_data = models.vehicles.objects.all()
    return render(request,'index.html',{'data':b_data})


def add_reservation(request):
    if request.method == "POST":
        h_name = request.POST.get('hotel_name')
        res_id = request.POST.get('hotelres_id')
        data = {'hotel_name':h_name,'hotelres_id':res_id,'user_id':'1'}
        serial = Serializers.ReservationSerializer(data=data)
        if serial.is_valid():
            try:
                serial.save()
                return render(request,'base.html')
            except:
                return render(request,'base.html')
    else:
        return render(request,'base.html')

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
