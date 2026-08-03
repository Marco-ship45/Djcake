from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),

    path('pasteles/', views.pasteles, name='pasteles'),

    path('noticias/', views.noticias, name='noticias'),

    path('contactos/', views.contactos, name='contactos'),

    path('enlaces/', views.enlaces, name='enlaces'),

]