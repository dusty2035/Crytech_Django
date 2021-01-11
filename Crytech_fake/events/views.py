from django.shortcuts import render , get_object_or_404
from django.core.paginator import EmptyPage , PageNotAnInteger , Paginator
from .models import Event
# Create your views here.


def events(request):
    event = Event.objects.order_by('-date')
    paginator = Paginator(event , 20)
    page = request.GET.get('page')

    try:
        Pevents = paginator.page(page)
    except PageNotAnInteger:
        Pevents = paginator.page(1)
    except EmptyPage:
        Pevents = paginator.page(paginator.num_pages)
    return render(request, 'events.html' , {'events': Pevents})


def event(request , event_id):
    event = get_object_or_404(Event , pk=event_id)
    return render(request, 'event.html' , {'event' : event})