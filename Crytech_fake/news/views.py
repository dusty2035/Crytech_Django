from django.shortcuts import render , get_object_or_404
from .models import New
from django.core.paginator import EmptyPage , PageNotAnInteger , Paginator
# Create your views here.


def news(request):
    news = New.objects.order_by('-date').all()
    paginator = Paginator(news , 20)
    page = request.GET.get('page')

    try:
        Pnews = paginator.page(page)
    except PageNotAnInteger:
        Pnews = paginator.page(1)
    except EmptyPage:
        Pnews = paginator.page(paginator.num_pages)
    

    return render(request , 'news.html' , {'news' : Pnews})


def news_s(request, news_id):
    news = get_object_or_404(New , pk=news_id)
    return render(request, 'news_s.html' , {'news_s' : news})

