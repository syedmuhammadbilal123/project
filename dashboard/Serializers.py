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
