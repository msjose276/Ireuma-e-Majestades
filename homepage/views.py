from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader



from .models import Cloth
from .models import Shoe
from .models import Hair


def index(request):
    list_of_clothes = Cloth.objects.order_by('title')
    list_of_shoes = Shoe.objects.order_by('title')
    list_of_hair = Hair.objects.order_by('title')

    # ----------------- start sections ------------------------
    chothes_cover = None
    shoes_cover = None
    hair_cover = None
    for cloth in list_of_clothes:
        if cloth.title == 'capa':
            chothes_cover = cloth

    for shoes in list_of_shoes:
        if shoes.title == 'capa':
            shoes_cover = shoes

    for hair in list_of_hair:
        if hair.title == 'capa':
            hair_cover = hair
    # ----------------- end of sections ------------------------


    # ----------------- start of featured ------------------------

    best_sellers = []
    # best_sellers = list_of_clothes + list_of_shoes + list_of_hair

    list_of_clothes = Cloth.objects.order_by('popularity')
    list_of_shoes = Shoe.objects.order_by('popularity')
    list_of_hair = Hair.objects.order_by('popularity')

    best_sellers_clothes = list_of_clothes[:5]
    best_sellers_shoes = list_of_shoes[:5]
    best_sellers_hair = list_of_hair[:5]

    best_sellers = best_sellers_clothes

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
        'list_of_clothes' : list_of_clothes,
        'list_of_shoes' : list_of_shoes,
        'list_of_hair' : list_of_hair,

        'chothes_cover' :chothes_cover,
        'shoes_cover' : shoes_cover,
        'hair_cover' : hair_cover,

        'best_sellers' : best_sellers,

        'best_sellers_clothes' : best_sellers_clothes,

        'list_of_sale' : list_of_sale,
    }
    return HttpResponse(template.render(context, request))



def section_detail(request,keyword):

    if keyword == 'Cloth' :
        list_of_items = Cloth.objects.order_by('title')
        section_title = 'Roupas'
    if keyword == 'Shoe' :
        list_of_items = Shoe.objects.order_by('title')
        section_title = 'Calcados'
    if keyword =='Hair' :
        list_of_items = Hair.objects.order_by('title')
        section_title = 'Cabelo'

    template = loader.get_template('section_detail.html')
    context = {
        'list_of_items' : list_of_items,
        'section_title' : section_title,
    }
    return HttpResponse(template.render(context, request))
