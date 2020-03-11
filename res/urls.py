# path('base/',views.Home)
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home),
    path('',views.Index),
    path('add_reservation',views.add_reservation),
    path('add_booking',views.add_booking)
]
