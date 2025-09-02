from django.shortcuts import render

from menu.models import Menu


# Create your views here.

def index(request):
    burgers = Menu.objects.all()

    context = {
        'burgers': burgers
    }

    return render(request, 'menu/index.html', context)

def menu(request):
    burgers = Menu.objects.all()

    context = {
        'burgers': burgers
    }

    return render(request, 'menu/menu.html', context)