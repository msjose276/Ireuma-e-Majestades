from django.contrib import admin
from .models import Cloth
from .models import Hair
from .models import Shoe
# Register your models here.



class ClothAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = ['title','price','data','popularity','sale','african_traje']

class ShoeAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = ['title','price','data','popularity','sale','african_traje']

class HairAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = ['title','price','data','popularity','sale']


#-----------------------------------------------------------------------------------
admin.site.register(Cloth, ClothAdmin)
admin.site.register(Shoe, ShoeAdmin)
admin.site.register(Hair, HairAdmin)
