from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from products.models import ProductCategory


@staff_member_required
def price_list_view(request):
    categories = ProductCategory.objects.prefetch_related('product_set')
    return render(request, 'products/price_list.html', {
        'categories': categories
    })
