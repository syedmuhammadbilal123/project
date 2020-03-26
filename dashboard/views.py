from django.shortcuts import render,redirect
from django.http import HttpResponse
from res.models import vendor
from django.contrib import messages
from dashboard.Serializers import RegistrationSerializer,EventsSerializer,VehicleSerializer



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

def makemytrip(request):
    return render(request,'makemytrip.html')

def property(request):
    return render(request,'property.html')

def vehicle(request):
    return render(request,'vehicle.html')

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
        v_name =  request.POST.get('vehiclename')
        v_type = request.POST.get('vehicletype')
        m_id = request.POST.get('modelid')
        m_name = request.POST.get('modelname')
        data = {'vehicles_id':v_name,'vehicles_name':v_name,'vehicle_type':v_type,'model_id':m_id,'model_name':m_name,'user_id':2}
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
            messages.error(request, 'Invalid Serializer')
            return redirect('reservation-vehicle')
    else:
        return render(request,'sorry.html')
