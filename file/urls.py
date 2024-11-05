from django.urls import path
from . import views  # Assuming views are in the same directory

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('uhome/', views.uhome, name='uhome'),
    path('about/', views.about, name='about'),
    path('watchdetails/', views.watchdetails, name='watchdetails'),
    path('bikedetails/', views.bikedetails, name='bikedetails'),
    path('cardetails/',views.cardetails,name='cardetails'),
    path('thar/',views.thar,name='thar'),
    path('rolex/',views.rolex,name='rolex'),
]
