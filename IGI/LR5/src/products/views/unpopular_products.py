from django.db.models import Sum
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from products.models import Product


@staff_member_required
def unpopular_products_view(request):
    unpopular_products = (
        Product.objects
        .annotate(total_sold=Sum('orderitem__quantity'))
        .filter(total_sold__isnull=True)
    )
    return render(request, 'products/unpopular_products.html', {
        'products': unpopular_products
    })