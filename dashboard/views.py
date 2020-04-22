from django.shortcuts import render,redirect
from django.http import HttpResponse
from res import models
from django.contrib import messages
from dashboard.Serializers import RegistrationSerializer,EventsSerializer,VehicleSerializer,HotelSerializer,ResturantSerializer



# Create your views here.


def dash(request):
    return render(request,'back.html')


def loginView(request):
    return render(request,'vendor_login.html')

def register(request):
    return render(request,'register.html')


def dashboard(request):
    return render(request,'dashboard.html')

def events(request):

    return render(request,'events.html')

def hotel(request):

    return render(request,'hotel.html')

def makemytrip(request):
    return render(request,'makemytrip.html')

def property(request):
    return render(request,'property.html')
def myresturant(request):
    resturant_t = res_table.objects.all()
    all_resturant = resturant.objects.all()
    return render(request,"resturant.html",{'resturant':resturant_t,'all_resturant':all_resturant})

def vehicle(request):

    vehicles_t = vehicles_type.objects.all()
    all_vehicles = vehicles.objects.all()

    return render(request,"vehicle.html",{'vehicles':vehicles_t,'all_vehicles':all_vehicles})



def showClients(request):
    vendor_hotels = list(models.hotel.objects.filter(user_id = 1).values_list('hotel_id', flat=True))
    hotel_room = list(models.room.objects.filter(hotel_id__in = vendor_hotels).values_list('room_id', flat=True))
    users_and_rooms_info = models.hotel_reservations.objects.filter(room_id__in = hotel_room)

    return render(request,'show_clients.html', context={"info": users_and_rooms_info})

def add_vendors(request):

    if request.method == "POST":
        n_name = request.POST.get('full_name')
        e_email = request.POST.get('email')
        p_password = request.POST.get('password')
        d_designation = request.POST.get('designation')
        data = {'vendor_name':n_name,'vendor_email':e_email,'vendor_password':p_password,'vendor_designation':d_designation,'role':2}
        serial = RegistrationSerializer(data=data)
        if serial.is_valid():
            try:
                serial.save()
                return render(request,'vendor_login.html')
            except:
                return render(request,'vendor_login.html')
    else:
        return render(request,'reigister.html')

def login_press(request):
    if request.method == "POST":
        n_email = request.POST.get('email')
        p_password = request.POST.get('password')
        v = vendor.objects.filter(vendor_email=n_email).last()
        if v == None:
            messages.error(request, n_email)
            return redirect('reservation-login')
        if v.vendor_email == n_email:
            if v.vendor_password == p_password:
                return render(request,'dashboard.html')
            else:
                return render(request,'vendor_login.html')
        else:
            return render(request,'vendor_login.html')
    else:
        return render(request, 'vendor_login.html')

def add_events(request):

    if request.method == "POST":
        e_name = request.POST.get('eventname')
        e_location = request.POST.get('eventlocation')
        e_type = request.POST.get('eventtype')
        e_price = request.POST.get('eventprice')
        e_time = request.POST.get('eventtime')
        data = {'event_name':e_name,'event_location':e_location,'event_type':e_type,'price':e_price,'time':e_time,'vendor_id':1}
        serial = EventsSerializer(data=data)
        if serial.is_valid():
            try:
                serial.save()
                messages.success(request, 'Saved')
                return redirect('reservation-events')
            except:
                messages.error(request, 'Something Wrong')
                return redirect('reservation-events')
        else:
            messages.error(request, 'Invalid Serializer')
            return redirect('reservation-events')
    else:
        return render(request,'sorry.html')

def add_vehicle(request):
    if request.method == "POST":
        v_name = request.POST.get('vehiclename')
        v_type = request.POST.get('vehicletype')
        m_id = request.POST.get('modelid')
        m_name = request.POST.get('modelname')
        data = {'vehicles_name':v_name,'vehicles_type':v_type,'model_id':m_id,'model_name':m_name,'user_id':'2'}
        #messages.success(request, data)
        serial = VehicleSerializer(data=data)


        if serial.is_valid():
            try:
                serial.save()
                messages.success(request, 'Saved')
                return redirect('reservation-vehicle')
            except:
                messages.error(request, 'Something Wrong')
                return redirect('reservation-vehicle')
        else:
            messages.success(request, serial.data)
            messages.error(request, 'Invalid Serializer')
            return redirect('reservation-vehicle')
    else:
        return render(request,'sorry.html')

def add_hotel(request):
    if request.method == "POST":
        h_name = request.POST.get('hotelname')
        h_type = request.POST.get('hoteltype')
        h_location = request.POST.get('hotellocation')

        data = {'hotel_name':h_name,'hotel_type':h_type,'hotel_location':h_location,'user_id':'2'}
        #messages.success(request, data)
        serial = HotelSerializer(data=data)


        if serial.is_valid():
            try:
                serial.save()
                messages.success(request, 'Saved')
                return redirect('reservation-hotel')
            except:
                messages.error(request, 'Something Wrong')
                return redirect('reservation-hotel')
        else:
            messages.success(request, serial.data)
            messages.error(request, 'Invalid Serializer')
            return redirect('reservation-hotel')
    else:
        return render(request,'sorry.html')


def add_my_resturant(request):
    if request.method == "POST":
        r_name = request.POST.get('resturantname')
        r_loc = request.POST.get('resturantlocation')
        r_table = request.POST.get('restable')
        r_type = request.POST.get('resturanttype')

        data = {'resturant_name':r_name,'resturant_location':r_loc,'res_table':r_table,'resturant_type':r_type,'user_id':'2'}
        #messages.success(request, data)
        serial = ResturantSerializer(data=data)


        if serial.is_valid():
            try:
                serial.save()
                messages.success(request, 'Saved')
                return redirect('reservation-myresturant')
            except:
                messages.error(request, 'Something Wrong')
                return redirect('reservation-myresturant')
        else:
            messages.success(request, serial.data)
            messages.error(request, 'Invalid Serializer')
            return redirect('reservation-myresturant')
    else:
        return render(request,'sorry.html')

