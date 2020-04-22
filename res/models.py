from django.db import models

# Create your models here.
class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)
    class Meta:
        db_table = "Roles"

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    role = models.ForeignKey(Roles,on_delete=models.CASCADE)
    class Meta:
        db_table = "User"

class vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=100)
    vendor_email = models.CharField(max_length=100)
    vendor_password = models.CharField(max_length=100)
    vendor_designation = models.CharField(max_length=100)
    role = models.ForeignKey(Roles,on_delete=models.CASCADE)
    class Meta:
        db_table = "vendor"

class hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=100)
    hotel_type = models.CharField(max_length=100)
    hotel_location = models.IntegerField()
    user_id = models.ForeignKey(Roles,on_delete=models.CASCADE)

    @property
    def displayname(self):
        return f'{self.hotel_name}'

    class Meta:
        db_table = "hotel"
class resturant(models.Model):
    resturant_id = models.AutoField(primary_key=True)
    resturant_name = models.CharField(max_length=100)
    resturant_location = models.CharField(max_length=100)
    res_table = models.ForeignKey("res_table",on_delete=models.CASCADE,default=None)
    resturant_type= models.CharField(max_length=100)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = "resturant"

class res_table(models.Model):
    res_table_id = models.AutoField(primary_key=True)
    no_of_seats = models.CharField(max_length=100)

    class Meta:
        db_table = "res_table"



class hotel_room(models.Model):
    hotel_room_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(hotel,on_delete=models.CASCADE)
   # room_id = models.ForeignKey(room,on_delete=models.CASCADE)
    class Meta:
        db_table = "hotel_room"

class room_type(models.Model):
    room_type_id = models.AutoField(primary_key=True)
    room_type_name = models.CharField(max_length=100,default=None)

    @property
    def displayname(self):
        return f'{self.room_type_name}'

    class Meta:
        db_table = "room_type"


class room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_price = models.CharField(max_length=100)
    no_of_persons = models.IntegerField()
    no_of_rooms = models.IntegerField(default=0)
    discount_rates = models.IntegerField(default=0)
    room_category = models.CharField(max_length=100)
    normal = models.CharField(max_length=100)
    pent_house = models.CharField(max_length=100)
    room_type = models.ForeignKey(room_type,on_delete=models.CASCADE,default=None)
    hotel_id = models.ForeignKey(hotel,on_delete=models.CASCADE)
    class Meta:
        db_table = "room"




class amenity(models.Model):
    floor_no = models.IntegerField()
    roof_available = models.BooleanField(default=False)
    hotWater_available = models.BooleanField(default=False)
    private_parking_available = models.BooleanField(default=False)
    rooms = models.ForeignKey(room,on_delete=models.CASCADE)
    class Meta:
        db_table = "amenity"



class total_price(models.Model):
    total_price_id = models.AutoField(primary_key=True)
    price = models.IntegerField(default=None)
    date = models.CharField(max_length=100)
    hotel_id = models.ForeignKey(hotel,on_delete=models.CASCADE)
    resturant_id = models.ForeignKey(resturant,on_delete=models.CASCADE)
    class Meta:
        db_table = "total_price"



class admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=100)
    admin_email = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=100)
    role_id = models.ForeignKey(Roles,on_delete=models.CASCADE)
    class Meta:
        db_table = "admin"




class resorts(models.Model):
    resort_id = models.AutoField(primary_key=True)
    resort_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    trip_id = models.ForeignKey(Roles,on_delete=models.CASCADE)
    class Meta:
        db_table = "resorts"

class event_places(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100)
    event_location = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    vendor_id = models.ForeignKey(vendor,on_delete=models.CASCADE,default=None)
    class Meta:
        db_table = "event_places"

class vehicles_type(models.Model):
    vehicles_type_id = models.AutoField(primary_key=True)
    vehicle_type_name = models.CharField(max_length=100)
    class Meta:
        db_table = "vehicles_type"

class vehicles(models.Model):
    vehicles_id = models.AutoField(primary_key=True)
    vehicles_name = models.CharField(max_length=100)
    vehicles_type = models.ForeignKey(vehicles_type,on_delete=models.CASCADE,default=None)
    model_id = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)

    user_id = models.ForeignKey(Roles,on_delete=models.CASCADE)


    class Meta:
        db_table = "vehicles"


class bus(models.Model):
   bus_id = models.AutoField(primary_key=True)
   bus_name = models.CharField(max_length=100)
   model_no = models.IntegerField()
   model_name = models.CharField(max_length=100)
   duration = models.CharField(max_length=100)
   routes_id = models.IntegerField()
   vehicles_id = models.ForeignKey(vehicles,on_delete=models.CASCADE)
   class Meta:
        db_table = "bus"


class rikshaw(models.Model):
    rikshaw_id = models.AutoField(primary_key=True)
    model_no = models.IntegerField()
    model_name = models.CharField(max_length=100)
    routes_id = models.IntegerField()
    duration = models.CharField(max_length=100)
    vehicles_id = models.ForeignKey(vehicles,on_delete=models.CASCADE)
    class Meta:
        db_table = "rikshaw"

class routes(models.Model):
    routes_id = models.AutoField(primary_key=True)
    no_of_stops = models.CharField(max_length=100)
    google_points = models.CharField(max_length=100)
    start_point = models.CharField(max_length=100)
    middle_point = models.CharField(max_length=100)
    End_point = models.CharField(max_length=100)
    vehicles_id = models.ForeignKey(vehicles,on_delete=models.CASCADE)
    class Meta:
        db_table = "routes"

class train_station(models.Model):
    train_station_id = models.AutoField(primary_key=True)
    train_station_name = models.CharField(max_length=100)
    no_of_persons = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    routes_id = models.ForeignKey(routes,on_delete=models.CASCADE)
    class Meta:
        db_table = "train_station"

class train(models.Model):
    train_id = models.AutoField(primary_key=True)
    train_name = models.CharField(max_length=100)
    stops = models.CharField(max_length=100)
    no_of_persons = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    routes_id = models.IntegerField()
    train_station_id = models.ForeignKey(train_station,on_delete=models.CASCADE)
    class Meta:
        db_table = "train"

class airlines(models.Model):
    airlines_id = models.AutoField(primary_key=True)
    airlines_name = models.CharField(max_length=100)
    no_of_persons = models.CharField(max_length=100)
    routes_id = models.ForeignKey(routes,on_delete=models.CASCADE)
    class Meta:
        db_table = "airlines"

class airplanes(models.Model):
    airplanes_id = models.AutoField(primary_key=True)
    airplanes_name = models.CharField(max_length=100)
    no_of_persons = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    starting_pt = models.CharField(max_length=100)
    end_pt = models.CharField(max_length=100)
    airlines_id = models.ForeignKey(airlines,on_delete=models.CASCADE)
    class Meta:
        db_table = "airplanes"




class hotel_reservations(models.Model):
    hotelres_id = models.AutoField(primary_key=True)
    check_in = models.CharField(max_length=100)
    check_out = models.CharField(max_length=100)
    day_arrival = models.CharField(max_length=100)
    time_duration = models.CharField(max_length=100)
    total_amount = models.FloatField(default=0.0)
    room_id = models.ForeignKey(room,on_delete=models.CASCADE,default='')
    user_id = models.ForeignKey(Roles,on_delete=models.CASCADE,default='')
    class Meta:
        db_table = "hotel_reservations"

class resturant_reservations(models.Model):
    restres_id = models.AutoField(primary_key=True)
    resturant_name = models.ForeignKey(resturant,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    total_price_id = models.ForeignKey(total_price,on_delete=models.CASCADE,default='')

    class Meta:
        db_table = "resturant_reservations"



class makeMyTrip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    tripprice = models.IntegerField()
    trip_duration = models.CharField(max_length=100)
    trip_facilities = models.CharField(max_length=100)
    hotel_id = models.ForeignKey(hotel,on_delete=models.CASCADE,default='')
    resturant_id = models.ForeignKey(resturant,on_delete=models.CASCADE,default='')
    resort_id = models.ForeignKey(resorts,on_delete=models.CASCADE,default='')
    event_id = models.ForeignKey(event_places,on_delete=models.CASCADE,default='')
    vehicles_id = models.ForeignKey(vehicles,on_delete=models.CASCADE,default='')
    routes_id = models.ForeignKey(routes,on_delete=models.CASCADE,default='')
    train_station_id = models.ForeignKey(train_station,on_delete=models.CASCADE,default='')
    airlines_id = models.ForeignKey(airlines,on_delete=models.CASCADE,default='')
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)





    class Meta:
        db_table = "makeMyTrip"
