

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    # path('/section_detail', views.section_detail, name='section_detail'),
    path('section_detail/<str:keyword>/', views.section_detail, name='section_detail'),
    # path('sale/', views.sale, name='sale'),
    path('best_sellers/', views.best_sellers, name='best_sellers'),
    path('new_arrivals/', views.new_arrivals, name='new_arrivals'),
    path('item/<str:keyword>/', views.single_item, name='single_item'),

]
