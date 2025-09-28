from django.shortcuts import render
from products.models import News


def news_list(request):
    news = News.objects.order_by('-published_at')
    return render(request, 'products/news_list.html', {'news': news})