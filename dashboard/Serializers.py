from rest_framework import serializers
from res import models


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.vendor
        fields = ('vendor_name','vendor_email','vendor_password','vendor_designation','role')


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.event_places
        fields = ('event_name','event_location','event_type','price','time','vendor_id')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.vehicles
        fields = ('vehicles_name','vehicles_type','model_id','model_name','user_id')

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.hotel
        fields = ('hotel_name','hotel_type','hotel_location','user_id')

class ResturantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.resturant
        fields = ('resturant_name','resturant_location','res_table','resturant_type','user_id')

