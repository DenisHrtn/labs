from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from products.models import Order, OrderItem, Product
from users.models import Customer
from products.models import News
from products.models.partner import Partner
from products.models.company import AboutCompany


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
    context['featured_products'] = Product.objects.filter(is_active=True)[:8]
    context['partners'] = Partner.objects.all()[:12]
    context['company'] = AboutCompany.objects.first()

    return render(request, 'dashboard/dashboard.html', context)


