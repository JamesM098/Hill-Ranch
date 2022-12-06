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
    path('show_farm/<farm_id>', views.show_farms, name = "show-farm"),
    path('single_cow/<cow_id>', views.single_cow, name = "single-cow"),
    path('single_farm/<farm_id>', views.single_farm, name = "single-farm"),
    path('show_cow/<cow_id>', views.show_cows, name = "show-cow"),
    path('show_farm/<farm_id>', views.show_farms, name = "show-farm"),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('meat', views.ProductLandingPageView.as_view(), name='landing'),


]
