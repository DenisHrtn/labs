from django.db.models import Sum, F
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from products.models import OrderItem


@staff_member_required
def client_sales_summary(request):
    client_summary = OrderItem.objects.values('order__customer__name', 'order__customer__city') \
        .annotate(total_quantity=Sum('quantity'), total_spent=Sum(F('quantity') * F('product__price'))) \
        .order_by('order__customer__name')

    return render(request, 'products/client_sales_summary.html',{
        'client_summary': client_summary
    })
