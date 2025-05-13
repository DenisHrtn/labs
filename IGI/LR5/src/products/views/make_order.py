from django.forms import formset_factory
from django.shortcuts import render
from django.shortcuts import redirect

from products.models import OrderItem
from products.forms.orders_form import OrderForm, OrderItemForm


def make_order(request):
    OrderItemFormSet = formset_factory(OrderItemForm, extra=1)

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        formset = OrderItemFormSet(request.POST)

        if order_form.is_valid() and formset.is_valid():
            order = order_form.save()
            for form in formset:
                product = form.cleaned_data.get('product')
                quantity = form.cleaned_data.get('quantity')
                if product and quantity:
                    OrderItem.objects.create(order=order, product=product, quantity=quantity)
            return redirect('product_list')  # или на страницу заказа

    else:
        order_form = OrderForm()
        formset = OrderItemFormSet()

    return render(request, 'products/make_order.html', {
        'order_form': order_form,
        'formset': formset
    })
