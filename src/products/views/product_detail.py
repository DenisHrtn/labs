from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from ..models import Product


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    return render(request, 'products/product_detail.html', {'product': product})


def add_to_cart_view(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    quantity = int(request.POST.get('quantity', 1))

    cart = request.session.get('cart', {})
    product_id_str = str(product.pk)

    if product_id_str in cart:
        cart[product_id_str] += quantity
    else:
        cart[product_id_str] = quantity

    request.session['cart'] = cart
    return redirect('cart_view')



