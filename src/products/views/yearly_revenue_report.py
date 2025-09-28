import json

from django.db.models import Sum, F, FloatField
from django.db.models.functions import ExtractYear
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from products.models import OrderItem


@staff_member_required
def yearly_revenue_report_view(request):
    revenue_by_year = (
        OrderItem.objects
        .annotate(year=ExtractYear('order__order_date'))
        .annotate(total=F('quantity') * F('product__price'))
        .values('year')
        .annotate(total_revenue=Sum('total', output_field=FloatField()))
        .order_by('year')
    )

    labels = [row['year'] for row in revenue_by_year]
    data = [row['total_revenue'] for row in revenue_by_year]

    context = {
        'revenue_by_year': revenue_by_year,
        'chart_labels': json.dumps(labels),
        'chart_data': json.dumps(data),
    }
    return render(request, 'products/yearly_revenue_report.html', context)
