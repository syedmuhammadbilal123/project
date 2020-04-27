from django.shortcuts import render,redirect
from res.models import hotel_reservations
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from rest_framework.response import Response
from django.contrib import messages
from res.Serializers import ReservationSerializer

from . import Serializers
from . import models

# Create your views here.
def Home(request):
    """docstring for Home"""
    hotels =  models.hotel.objects.all()
    return render(request,'reservation.html',{'hotels':hotels})

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

def get_rooms(request):

        if request.method == 'GET':
               hotel_id = request.GET['hotel_id']

               rooms_data = rooms.objects.filter(hotel_id=post_id)
               return HttpResponse(rooms_data) # Sending an success response
        else:
               return HttpResponse("Request method is not a GET")


def add_reservation(request):

    if request.method == "POST":

        # h_name = request.POST.get('hotel-name')
        c_in = str(request.POST.get('checkin'))
        c_out = str(request.POST.get('checkout'))
        d_arrival = request.POST.get('day')
        t_duration = request.POST.get('time')
        t_amount = float(request.POST.get('amount'))
        room_id = request.POST.get('hotel_and_room')
        hotel_id = room_id.split("|")[1]
        reserved_room = list(models.hotel_reservations.objects.filter(room_id = room_id.split("|")[0]).values_list('room_id', flat=True))
        reserved_hotel_room = len(models.room.objects.filter(hotel_id=hotel_id))

        if reserved_hotel_room < 4:

            data = {'check_in':c_in,'check_out':c_out,'day_arrival':d_arrival,'time_duration':t_duration,'total_amount':t_amount,'room_id': room_id.split("|")[0],'user_id':'1'}

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
            messages.error(request, 'Room is not available right now!')
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
