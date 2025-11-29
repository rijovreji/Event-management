from django.db import models

# Create your models here.
class Event(models.Model):
    img= models.ImageField(upload_to="pic")
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Booking(models.Model):
    cust_Name=models.CharField(max_length=55,null=True,blank=True)
    cust_Phn=models.IntegerField(null=True,blank=True)
    Name=models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    Booking_on=models.DateField(auto_now=True)
