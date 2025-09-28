from django.shortcuts import render, get_object_or_404
from products.models import News


def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'products/news_detail.html', {'news_item': news_item})
