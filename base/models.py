from django.db import models

# Create your models here.
 
class Address(models.Model):
    house_no = models.CharField(max_length = 255)
    Street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    country = models.CharField(max_length = 255)

class  Car(models.Model):
    c_id = models.SmallIntegerField()
    brand = models.CharField(max_length = 255)
    model = models.CharField(max_length = 255)
    number_plate = models.PositiveIntegerField()

class Ads(models.Model):
    a_id = models.SmallIntegerField()
    title = models.CharField(max_length = 255)
    description = models.TextField()
    price_per_km = models.DecimalField(max_digits = 6,decimal_places = 2)

class User(models.Model):
    u_id = models.SmallIntegerField()
    f_name = models.CharField(max_length = 255)
    l_name = models.CharField(max_length = 255)
    age = models.PositiveIntegerField()
    address = models.ForeignKey(Address , on_delete = models.CASCADE)
    car = models.ForeignKey(Car , on_delete = models.CASCADE)
    ads = models.ForeignKey(Ads , on_delete = models.CASCADE)
