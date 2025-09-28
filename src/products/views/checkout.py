from django import forms
from django.shortcuts import render, redirect
from products.models import Product


class CheckoutForm(forms.Form):
    full_name = forms.CharField(label='ФИО', max_length=255)
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Адрес', widget=forms.Textarea)
    card_number = forms.CharField(label='Номер карты', max_length=19)
    expiry = forms.CharField(label='Срок', max_length=5, help_text='MM/YY')
    cvc = forms.CharField(label='CVC', max_length=4)
    agree = forms.BooleanField(label='Согласен с политикой конфиденциальности')


def checkout_view(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart_view')

    # Подсчитываем общую сумму
    total = 0
    cart_items = []
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

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            request.session['cart'] = {}
            return render(request, 'products/checkout_success.html', {'data': form.cleaned_data})
    else:
        form = CheckoutForm()

    return render(request, 'products/checkout.html', {
        'form': form, 
        'total': total,
        'cart_items': cart_items
    })



