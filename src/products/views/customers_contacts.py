from django.shortcuts import render
from users.models import Customer


def customer_contacts_view(request):
    customers = Customer.objects.select_related('user')
    return render(request, 'products/customer_contacts.html', {'customers': customers})
