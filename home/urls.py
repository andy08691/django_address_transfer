from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('geoprocessing', views.get_geo_location),
]