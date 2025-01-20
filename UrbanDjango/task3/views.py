from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def platform(request):
    name_1 = 'Главная страница'
    context = {'name_1': name_1}
    return render(request, 'platform.html', context)


def games(request):
    name2 = 'Игры'
    g1 = 'super mario'
    g2 = 'tank1990'
    g3 = 'mortal combat'
    buy = 'купить'
    context = {'g1': g1, 'g2': g2, 'g3': g3, 'buy': buy, 'Title': name2}
    return render(request, 'games.html', context)


def cart(request):
    return render(request, 'cart.html')
