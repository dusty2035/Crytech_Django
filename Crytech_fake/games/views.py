from django.shortcuts import render, get_object_or_404
from .models import Game 
# Create your views here.


def game(request):
    game = Game.objects.all().order_by('game_title')
    return render(request , 'games.html' , {'games' : game})


def game_s(request , game_title):
    game = Game.objects.all().order_by('game_title')
    game_s = get_object_or_404(Game , pk=game_title)
    return render(request , 'game.html' , {'game' : game_s , 'games' : game})