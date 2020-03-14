from django.shortcuts import render,redirect
from django.http import HttpResponse
from res.models import vendor
from dashboard.Serializers import RegistrationSerializer,EventsSerializer



# Create your views here.


def dash(request):
    return render(request,'back.html')


def login(request):
    return render(request,'login.html')

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
                return render(request,'login.html')
            except:
                return render(request,'login.html')
    else:
        return render(request,'reigister.html')

def login_press(request):
    if request.method == "POST":
        n_name = request.POST.get('name')
        p_password = request.POST.get('password')
        v = vendor.objects.filter(vendor_name=n_name).last()
        if v.vendor_name == n_name:
            if v.vendor_password == p_password:
                return render(request,'dashboard.html')
            else:
                return render(request,'login.html')
        else:
            return render(request,'login.html')

def add_events(request):

    if request.method == "POST":
        e_name = request.POST.get('eventname')
        e_location = request.POST.get('eventlocation')
        e_type = request.POST.get('eventtype')
        e_price = request.POST.get('eventprice')
        e_time = request.POST.get('eventtime')
        data = {'event_name':e_name,'event_location':e_location,'event_type':e_type,'price':e_price,'time':e_time}
        serial = EventsSerializer(data=data)
        if serial.is_valid():
            try:
                serial.save()
                return render(request,'submitted.html')
            except:
                return render(request,'login.html')
        else:
            return render(request,'sorry.html')
    else:
        return render(request,'sorry.html')
def add_vehicle(request):
    if request.method == "POST":
        v_name =  request.POST.get('vehiclename')
        v_type = request.POST.get('vehicletype')
        m_id = request.POST.get('modelid')
        m_name = request.POST.get('modelname')
        vehicle_data = {'vehicles_id':v_name,'vehicles_name':v_name,'vehicle_type':v_type,'model_id':modelid,'model_name':modelname}
        serial = VehicleSerializer(vehicle_data=vehicle_data)
        if serial.is_valid():
            try:
                serial.save()
                return render(request,'submitted.html')
            except:
                return render(request,'login.html')
    else:
        return render(request,'sorry.html')
