from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Cloth
from .models import Shoe
from .models import Hair
from .models import Section
from .models import Item
from .models import PhotoItem




def index(request):
    list_of_section = Section.objects.order_by('title')

    # get the 10 best seller items
    list_of_best_sellers = Item.objects.order_by('-popularity')
    best_sellers = list_of_best_sellers[:4]

    template = loader.get_template('index.html')
    context = {
        'list_of_section' : list_of_section,
        'best_sellers' : best_sellers,


    }
    return HttpResponse(template.render(context, request))



def section_detail(request,keyword):

    list_of_items = Item.objects.filter(type=keyword)
    template = loader.get_template('section_detail.html')
    context = {
        'list_of_items' : list_of_items,
        'section_title' : keyword,
    }
    return HttpResponse(template.render(context, request))

def best_sellers(request):

    list_of_best_sellers = Item.objects.filter(sale=True)

    list_of_best_sellers = Item.objects.order_by('-popularity')
    list_of_items = list_of_best_sellers[:4]

    template = loader.get_template('section_detail.html')

    section_title = 'Promoção'
    context = {
        'list_of_items' : list_of_items,
        'section_title' : section_title,
    }
    return HttpResponse(template.render(context, request))


def new_arrivals(request):
    list_of_new_arrivals = Item.objects.order_by('-date')
    list_of_items = list_of_new_arrivals[:40]
    template = loader.get_template('section_detail.html')

    section_title = 'Novas Chegadas'
    context = {
        'list_of_items' : list_of_items,
        'section_title' : section_title,
    }
    return HttpResponse(template.render(context, request))



def single_item(request,keyword):
    item = Item.objects.filter(id=keyword)
    photos = PhotoItem.objects.filter(item_name=item[0].id)
    section_title = item[0].title
    photos_lenght = len(photos)

    # get the 10 best seller items
    list_of_best_sellers = Item.objects.order_by('-popularity')
    best_sellers = list_of_best_sellers[:10]

    template = loader.get_template('one_item.html')
    context = {
        'item' : item[0],
        'photos' : photos,
        'section_title' : section_title,
        'photos_lenght' : photos_lenght,
        'best_sellers' : best_sellers,
    }
    return HttpResponse(template.render(context, request))
