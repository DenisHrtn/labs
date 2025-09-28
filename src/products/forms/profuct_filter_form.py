from django import forms
from products.models import ProductCategory


class ProductFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=ProductCategory.objects.all(),
        required=False,
        label="Категория"
    )
    min_price = forms.DecimalField(required=False, label="Мин. цена")
    max_price = forms.DecimalField(required=False, label="Макс. цена")
