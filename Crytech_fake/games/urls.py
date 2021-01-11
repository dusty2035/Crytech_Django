from django.urls import path
from . import views

urlpatterns = [
    path('' , views.game , name = 'games'),
    path('<str:game_title>/' , views.game_s , name = 'game'),
]
