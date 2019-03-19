

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    # path('/section_detail', views.section_detail, name='section_detail'),
    path('<str:keyword>/', views.section_detail, name='section_detail'),
]
