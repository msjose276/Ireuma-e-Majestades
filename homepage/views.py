from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader



from .models import Cloth
from .models import Shoe
from .models import Hair
from .models import Section
from .models import Item


def index(request):
    list_of_section = Section.objects.order_by('title')

    # get the 10 best seller items
    list_of_best_sellers = Item.objects.order_by('-popularity')
    best_sellers = list_of_best_sellers[:4]


    # ----------------- start of featured ------------------------


    # best_sellers = list_of_clothes + list_of_shoes + list_of_hair

    # list_of_clothes = Cloth.objects.order_by('popularity')
    # list_of_shoes = Shoe.objects.order_by('popularity')
    # list_of_hair = Hair.objects.order_by('popularity')
    #
    # best_sellers_clothes = list_of_clothes[:5]
    # best_sellers_shoes = list_of_shoes[:5]
    # best_sellers_hair = list_of_hair[:5]
    #
    # best_sellers = best_sellers_clothes

    # ------------------ end of featured -----------------------


    # ------------------ start of sale -----------------------
    list_of_sale = None

    clothes_sale = Cloth.objects.filter(sale=True)
    shoes_sale = Shoe.objects.filter(sale=True)
    hair_sale = Hair.objects.filter(sale=True)
    list_of_sale = clothes_sale
    # ------------------- end of sale ----------------------

    # photos = PhotoClothing.objects.filter()
    template = loader.get_template('index.html')
    context = {
        'list_of_section' : list_of_section,

        'best_sellers' : best_sellers,

        'list_of_sale' : list_of_sale,
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

# def best_sellers(request):
#
#     list_of_items = Item.objects.filter(type=keyword)
#     template = loader.get_template('section_detail.html')
#     context = {
#         'list_of_items' : list_of_items,
#         'section_title' : keyword,
#     }
#     return HttpResponse(template.render(context, request))

def best_sellers(request):
    #
    # list_of_best_sellers = Item.objects.order_by('-popularity')
    # best_sellers = list_of_best_sellers[:4]

    # list_of_best_sellers = Item.objects.order_by('-popularity')

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
    #
    list_of_new_arrivals = Item.objects.order_by('-date')
    list_of_items = list_of_new_arrivals[:40]

    template = loader.get_template('section_detail.html')

    section_title = 'Novas Chegadas'
    context = {
        'list_of_items' : list_of_items,
        'section_title' : section_title,
    }
    return HttpResponse(template.render(context, request))
