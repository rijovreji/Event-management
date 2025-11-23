from django.db import models

# Create your models here.
class Event(models.Model):
    img= models.ImageField(upload_to="pic")
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)