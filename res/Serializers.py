from rest_framework import serializers
from . import models


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.hotel_reservations
        fields = ('hotelres_id','hotel_name','user_id')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.vehicles
        fields = ('vehicles_id','vehicles_name','vehicles_type','model_id','model_name')
