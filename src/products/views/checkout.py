from datetime import date, timedelta

from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from products.models import Product, Order, OrderItem
from users.models import Customer


class CheckoutForm(forms.Form):
    full_name = forms.CharField(label='ФИО', max_length=255)
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Адрес', widget=forms.Textarea)
    card_number = forms.CharField(label='Номер карты', max_length=19)
    expiry = forms.CharField(label='Срок', max_length=5, help_text='MM/YY')
    cvc = forms.CharField(label='CVC', max_length=4)
    agree = forms.BooleanField(label='Согласен с политикой конфиденциальности')


@login_required
def checkout_view(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Ваша корзина пуста.')
        return redirect('cart_view')

    total = 0
    cart_items = []
    products = Product.objects.filter(id__in=cart.keys())

    for product in products:
        quantity = cart[str(product.id)]
        item_total = product.price * quantity
        total += item_total
        cart_items.append({'product': product, 'quantity': quantity})

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                current_customer = Customer.objects.get(user=request.user)
            except Customer.DoesNotExist:
                messages.error(request, 'Не удалось найти ваш профиль покупателя. Обратитесь в поддержку.')
                return redirect('checkout_view')

            order = Order.objects.create(
                customer=current_customer,
                order_date=date.today(),
                delivery_date=date.today() + timedelta(days=3)
            )

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                )

            request.session['cart'] = {}

            return render(request, 'products/checkout_success.html', {
                'data': form.cleaned_data
            })
    else:
        form = CheckoutForm()

    return render(request, 'products/checkout.html', {
        'form': form,
        'total': total
    })

