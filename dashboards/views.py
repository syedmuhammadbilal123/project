from django.shortcuts import render,redirect
from django.http import HttpResponse
from res import models
#from django.core.urlresolvers import reverse_lazy
#from django.views.generic import DeleteView


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

# class eventsDeleteView(DeleteView):
#     template_name = 'templates/event_create.html'
#     context_oject_name = 'event_places.objects.all()'
#     success_url = reverse_lazy('event_places')

#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(events,id=id_)

def all_vehicles(request):
    vehicles = models.vehicles.objects.all()
    return render(request,"Vendor_Vehicles.html",{"data":vehicles})
def all_reservations(request):
    hotel_res = models.hotel_reservations.objects.all()
    return render(request,"Reserved_users.html",{"data":hotel_res})

