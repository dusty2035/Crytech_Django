from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup , name = "signup"),
    path('login/', views.login , name = "login"),
    path('logout/', views.logout , name = 'logout'),
    path('loged_in/', views.loged_in , name = 'logedin'),
    path('loged_in/edit/' , views.edit_profile , name = 'edit_profile'),
]
