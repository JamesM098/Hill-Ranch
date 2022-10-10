from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add-cow', views.add_cow, name = 'add-cow'),
    path('add-location', views.add_location, name = 'add-location'),
    path('farms/', views.farms, name = 'farms_url'),
    path('farms/all-farms/', views.all_farms, name = 'farms'),
    path('cows/', views.cows, name = "cows_url"),
    path('cows/all-cows/', views.all_cows, name = "cows"),
    path('show_cow/<cow_id>', views.show_cows, name = "show-cow"),
    path('show_farm/<farm_id>', views.show_farms, name = "show-farm"),
    path('meat', views.show_cows, name = "meat"),


]
