from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'home',
        'content': 'Главная страничка'
    } 
    
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('dasda')
