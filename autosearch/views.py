from re import search
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from .models import *

def generate_data(request):
    fake=searchoption.objects.all()
    for i in range(0 , 100):
        searchoption.objects.create(address=fake.address())
    return JsonResponse({'status' : 200})




def home(request):
    return render(request, 'index.html')



def search_address(request):
    search = request.GET.get('address')
    payload = []
    if search:
        searched_objs = searchoption.objects.filter(address__icontains=search)
        
        for searched_obj in searched_objs:
            payload.append(searched_obj.address)


    return JsonResponse({'status' : 200 , 'data' : payload})

















