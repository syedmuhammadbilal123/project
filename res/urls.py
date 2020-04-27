# path('base/',views.Home)
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('reservation/',views.Home,name='reservation-reservations'),
    path('login/',views.login),
    path('loginPressed',views.login_Pressed),
    # path('',views.Index),
    path('reservation/add_reservation',views.add_reservation, name='post'),
    path('dashvendor/',include('dashboard.urls'),name="dash_vendor"),
    path('add_booking',views.add_booking),
    path('getrooms/',views.get_rooms)
]
