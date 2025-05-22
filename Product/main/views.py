import re
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories 

def index(request):

    context = {
        'title': 'Home - Главная',
        'content': "Ювелирый магазин Efremova",
    } 
    
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')
