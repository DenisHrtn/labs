from django import forms
from products.models import Order, OrderItem, Product
from users.models import Customer


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'order_date', 'delivery_date']


class OrderItemForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.filter(is_active=True))
    quantity = forms.IntegerField(min_value=1)