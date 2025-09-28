from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import render
from django.db.models import Count
from users.models import Customer


@staff_member_required
def customers_by_city_view(request):
    cities = (
        Customer.objects
        .values('city')
        .annotate(count=Count('id'))
        .order_by('city')
    )

    customers_by_city = {}
    for city in cities:
        city_name = city['city']
        customers = Customer.objects.filter(city=city_name)
        customers_by_city[city_name] = customers

    return render(request, 'users/customers_by_city.html', {
        'customers_by_city': customers_by_city
    })
