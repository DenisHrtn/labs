from django.shortcuts import render
from django.db.models import Q

from products.models import Product
from common_services.permissions.login_permissions import login_required_redirect


@login_required_redirect
def search_products_view(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = Product.objects.filter(
            Q(name__icontains=query)
        ).order_by('name')

    return render(request, 'products/search_results.html', {
        'query': query,
        'results': results
    })
