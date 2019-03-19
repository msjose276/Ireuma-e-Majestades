from django.db import models
from django.utils import timezone


# Create your models here.

class Cloth(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100,default="blusa")
    price = models.IntegerField(default=0)
    data = models.DateTimeField(default=timezone.now)
    sale = models.BooleanField(default=False)
    african_traje = models.BooleanField(default=False)
    artwork = models.ImageField(upload_to='uploads/clothes/', default= " ",blank=False,max_length=45)
    #artwork = models.ImageField(upload_to='uploads/projects/', max_length=45, blank=True)
    popularity = models.IntegerField(default=0)


class Shoe(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    data = models.DateTimeField(default=timezone.now)
    sale = models.BooleanField(default=False)
    african_traje = models.BooleanField(default=False)
    artwork = models.ImageField(upload_to='uploads/shoes/', default= " ",blank=False,max_length=45)
    popularity = models.IntegerField(default=0)

class Hair(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    data = models.DateTimeField(default=timezone.now)
    sale = models.BooleanField(default=False)
    artwork = models.ImageField(upload_to='uploads/hair/', default= " ",blank=False,max_length=45)
    popularity = models.IntegerField(default=0)
