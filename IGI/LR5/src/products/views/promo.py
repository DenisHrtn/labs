from django.shortcuts import render
from django.utils import timezone
from products.models import PromoCode


def promo_list_view(request):
    today = timezone.now().date()
    promos = PromoCode.objects.filter(is_active=True, valid_from__lte=today)

    return render(request, 'products/promo_list.html', {
        'promos': promos
    })