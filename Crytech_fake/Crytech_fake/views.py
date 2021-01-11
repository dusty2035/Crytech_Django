from django.shortcuts import render
from events.models import Event
from news.models import New
from django.template import RequestContext

def homepage(request):
    event = Event.objects.order_by('-date')[:6]
    news = New.objects.order_by('-date')[:3]
    return render(request, 'home.html' , {'event' : event , 'news' : news})


def handler404(request , excepton):
    response = render("404.html")
    response.status_code = 404
    return response


def handler500(request):
    response = render(request,"404.html")
    response.status_code = 500
    return response