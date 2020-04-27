from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('back/',views.dash),
    path('login/',views.loginView,name='reservation-login'),
    path('login/login-Pressed',views.login_press),
    path('register/',views.register),
    path('',views.dashboard),
    path('events/',views.events,name='reservation-events'),
    path('hotel/',views.hotel,name='reservation-hotel'),
    path('makemytrip/',views.makemytrip),
    path('show/clients/',views.showClients),


    path('vehicle/',views.vehicle,name='reservation-vehicle'),
    path('myresturant/',views.myresturant,name='reservation-myresturant'),
    path('register/add_vendor', views.add_vendors),
    path('events/add_events', views.add_events),
    path('vehicle/add_vehicle',views.add_vehicle),
    path('myresturant/add_my_resturant',views.add_my_resturant),
    path('hotel/add_hotel',views.add_hotel),
    path('register/login_press', views.login_press),
    path('register/login_press/events',views.add_events),
    path('register/login_press/events/vehicles',views.add_vehicle)
]
