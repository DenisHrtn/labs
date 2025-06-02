from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from products.models import Order, OrderItem, Product
from users.models import Customer
from products.models import News


def dashboard_view(request):
    user = request.user
    context = {}

    if user.is_authenticated:
        if user.is_customer:
            customer = user.pk

            context['orders'] = Order.objects.filter(customer=customer).prefetch_related('products')
            context['title'] = 'Личный кабинет покупателя'

        elif user.is_client:
            context['orders'] = Order.objects.all().prefetch_related('products', 'customer')
            context['title'] = 'Кабинет сотрудника'

    else:
        context['orders'] = []
        context['title'] = 'Общий дашборд: каталог, отзывы, купоны'

    context['latest_news'] = News.objects.order_by('-published_at').first()

    return render(request, 'dashboard/dashboard.html', context)


