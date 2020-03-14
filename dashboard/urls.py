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
    path('makemytrip/',views.makemytrip),
    path('property/',views.property),
    path('vehicle/',views.vehicle),
    path('register/add_vendor', views.add_vendors),
    path('events/add_events', views.add_events),
    path('register/login_press', views.login_press),
    path('register/login_press/events',views.add_events),
    path('register/login_press/events/vehicles',views.add_vehicle)
]
