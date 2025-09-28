from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from products.models import Product


def cart_view(request):
    """Отображение корзины покупок"""
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    
    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            item_total = float(product.price) * quantity
            total += item_total
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total': item_total
            })
        except Product.DoesNotExist:
            continue
    
    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'products/cart.html', context)


def cart_add_item(request, product_id):
    """Добавление товара в корзину"""
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1
    
    request.session['cart'] = cart
    messages.success(request, f'{product.name} добавлен в корзину')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'message': 'Товар добавлен в корзину'})
    
    return redirect('product_detail', pk=product_id)


def cart_remove_item(request, product_id):
    """Удаление товара из корзины"""
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart
        messages.success(request, 'Товар удален из корзины')
    
    return redirect('cart_view')


def cart_update_qty(request, product_id):
    """Обновление количества товара в корзине"""
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        product_id_str = str(product_id)
        
        if quantity > 0:
            cart[product_id_str] = quantity
        else:
            cart.pop(product_id_str, None)
        
        request.session['cart'] = cart
        messages.success(request, 'Количество обновлено')
    
    return redirect('cart_view')


def cart_increase(request, product_id):
    """Увеличение количества товара в корзине"""
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1
    
    request.session['cart'] = cart
    messages.success(request, 'Количество увеличено')
    
    return redirect('cart_view')


def cart_decrease(request, product_id):
    """Уменьшение количества товара в корзине"""
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        if cart[product_id_str] > 1:
            cart[product_id_str] -= 1
        else:
            del cart[product_id_str]
        request.session['cart'] = cart
        messages.success(request, 'Количество уменьшено')
    
    return redirect('cart_view')
