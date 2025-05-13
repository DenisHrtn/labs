import json

from collections import defaultdict
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import render

from products.models import ProductCategory
from products.models import OrderItem


@staff_member_required
def monthly_sales_by_category_view(request):
    sales_data = (
        OrderItem.objects
        .select_related('product__category', 'order')
        .annotate(month=TruncMonth('order__order_date'))
        .values('month', 'product__category__name')
        .annotate(total_quantity=Sum('quantity'))
        .order_by('month', 'product__category__name')
    )

    chart_data = defaultdict(lambda: defaultdict(int))
    categories_set = set()
    for row in sales_data:
        month = row['month'].strftime('%Y-%m')
        category = row['product__category__name']
        categories_set.add(category)
        chart_data[month][category] = row['total_quantity']

    categories = sorted(categories_set)
    months = sorted(chart_data.keys())

    datasets = []
    for category in categories:
        datasets.append({
            'label': category,
            'data': [chart_data[month].get(category, 0) for month in months],
        })

    context = {
        'sales_data': sales_data,
        'chart_labels': json.dumps(months),
        'chart_datasets': json.dumps(datasets),
    }
    return render(request, 'products/monthly_sales_by_category.html', context)
