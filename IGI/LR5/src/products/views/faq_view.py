from django.shortcuts import render
from products.models import FAQ


def faq_view(request):
    faqs = FAQ.objects.all().order_by('-created_at')
    return render(request, 'products/faq.html', {'faqs': faqs})
