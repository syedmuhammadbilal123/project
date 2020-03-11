from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('backs/',views.backs),
    path('dashboards/',views.dashboards),
    path('login/',views.login),
    path('register/',views.register),
    path('train_schedule',views.train_schedule),
    path('airplane_schedule',views.airplane_schedule)

]
