from django.db import models
from django.utils import timezone


# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100,default="Roupa")
    price = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    sale = models.BooleanField(default=False)
    african_traje = models.BooleanField(default=False)
    artwork = models.ImageField(upload_to='uploads/items/', default= " ",blank=False,max_length=45)
    #artwork = models.ImageField(upload_to='uploads/projects/', max_length=45, blank=True)
    popularity = models.IntegerField(default=0)


# Similar to Color, Photo can be featured alongside Project.
# Multiple instances of Photo can also be created in the admin panel.
class PhotoItem(models.Model):
    item_name = models.ForeignKey(Item,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='uploads/item/photo', max_length=45)
    def projectTitle(self):
        return self.item_name.title


class Cloth(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100,default="blusa")
    price = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    sale = models.BooleanField(default=False)
    african_traje = models.BooleanField(default=False)
    artwork = models.ImageField(upload_to='uploads/clothes/', default= " ",blank=False,max_length=45)
    #artwork = models.ImageField(upload_to='uploads/projects/', max_length=45, blank=True)
    popularity = models.IntegerField(default=0)


class Shoe(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    sale = models.BooleanField(default=False)
    african_traje = models.BooleanField(default=False)
    artwork = models.ImageField(upload_to='uploads/shoes/', default= " ",blank=False,max_length=45)
    popularity = models.IntegerField(default=0)

class Hair(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    sale = models.BooleanField(default=False)
    artwork = models.ImageField(upload_to='uploads/hair/', default= " ",blank=False,max_length=45)
    popularity = models.IntegerField(default=0)


class Section(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    artwork = models.ImageField(upload_to='uploads/sections/', default= " ",blank=False,max_length=45)
