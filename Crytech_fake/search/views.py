from django.shortcuts import render
from products.models import Product
from news.models import New
from events.models import Event
from games.models import Game

# Create your views here.

def search(request):

    if request.method == 'GET':
        input = request.GET.get('search')

    results = {}
    if input :
        games = Game.objects.filter(game_title__icontains = input)
        products = Product.objects.filter(game_title__icontains = input)
        news = New.objects.filter(content__icontains = input)
        events = Event.objects.filter(content__icontains = input)
        if games or products or news or events :
            x = False
        else :
            x = True
    
        results =  {
        'games' : games,
        'products' : products,
        'news' : news ,
        'events' : events ,
        'x' : x ,
        }



    return render(request, 'search.html' , results)