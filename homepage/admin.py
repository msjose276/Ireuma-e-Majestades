from django.contrib import admin
from .models import Cloth
from .models import Hair
from .models import Shoe
from .models import Section
from .models import Item
from .models import PhotoItem


#------------------------------- Item photo ----------------------------------------------------
class PhotoItemInline(admin.TabularInline):
    model = PhotoItem

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    ordering = ['type']
    list_display = ['type','title','price','date','popularity','sale','african_traje']
    inlines = [PhotoItemInline]


class ClothAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = ['title','price','date','popularity','sale','african_traje']

class ShoeAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = ['title','price','date','popularity','sale','african_traje']

class HairAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = ['title','price','date','popularity','sale']


class SectionAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = ['title','date']

#-----------------------------------------------------------------------------------
admin.site.register(Item, ItemAdmin)
admin.site.register(Cloth, ClothAdmin)
admin.site.register(Shoe, ShoeAdmin)
admin.site.register(Hair, HairAdmin)
admin.site.register(Section, SectionAdmin)
