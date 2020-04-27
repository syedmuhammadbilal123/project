from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('backs/',views.backs),
    path('',views.dashboards,name="admin-dashboard"),
    path('login/',views.login),
    path('vendor_events/',views.all_Events),
    path('vendor_vehicles/',views.all_vehicles),
    path('user_reservations/',views.all_reservations),
    #path('delete/',eventsDeleteView.as_view(),name='event-delete'),
    # path('register/',views.register),
    path('train_schedule',views.train_schedule),
    path('airplane_schedule',views.airplane_schedule)

]
