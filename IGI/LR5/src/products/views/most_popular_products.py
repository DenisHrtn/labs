from django.db.models import Sum
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from products.models import Product


@staff_member_required
def most_popular_products_view(request):
    popular_products = (
        Product.objects
        .annotate(total_sold=Sum('orderitem__quantity'))
        .filter(total_sold__gt=0)
        .order_by('-total_sold')
    )
    return render(request, 'products/most_popular_products.html', {
        'products': popular_products
    })
