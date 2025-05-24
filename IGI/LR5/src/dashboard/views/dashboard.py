from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from products.models import Order, OrderItem, Product
from users.models import Customer


def dashboard_view(request):
    user = request.user
    context = {}

    if user.is_authenticated:
        if user.is_customer:
            try:
                customer = Customer.objects.get(user=user)
            except Customer.DoesNotExist:
                customer = None

            if customer:
                context['orders'] = Order.objects.filter(customer=customer).prefetch_related('products')
            else:
                context['orders'] = []

            context['title'] = 'Личный кабинет покупателя'

        elif user.is_client:
            context['orders'] = Order.objects.all().prefetch_related('products', 'customer')
            context['title'] = 'Кабинет сотрудника'
    else:
        context['orders'] = []
        context['title'] = 'Общий дашборд: каталог, отзывы, купоны'

    return render(request, 'dashboard/dashboard.html', context)


