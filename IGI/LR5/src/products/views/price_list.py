from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from products.models import ProductCategory
from common_services.permissions.login_permissions import login_required_redirect


@login_required_redirect
def price_list_view(request):
    categories = ProductCategory.objects.prefetch_related('product_set')
    return render(request, 'products/price_list.html', {
        'categories': categories
    })
