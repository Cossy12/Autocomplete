from django.urls import path
from . import views

urlpatterns = [
    path('generate/' , views.generate_data),
    path('search/' , views.search_address),
    
    
    path('' , views.home),
]