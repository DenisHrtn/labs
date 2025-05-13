from django.shortcuts import render

from products.models import Product
from products.forms.profuct_filter_form import ProductFilterForm


def product_list(request):
    products = Product.objects.filter(is_active=True)
    form = ProductFilterForm(request.GET)

    if form.is_valid():
        if form.cleaned_data.get('category'):
            products = products.filter(category=form.cleaned_data['category'])
        if form.cleaned_data.get('min_price'):
            products = products.filter(price__gte=form.cleaned_data['min_price'])
        if form.cleaned_data.get('max_price'):
            products = products.filter(price__lte=form.cleaned_data['max_price'])

    return render(request, 'products/product_list.html', {
        'products': products,
        'form': form
    })
