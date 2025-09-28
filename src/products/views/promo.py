from django.shortcuts import render
from products.models import PromoCode
from django.shortcuts import redirect
from django.contrib import messages
from django.utils import timezone
from products.forms.promo_form import PromoCodeForm


def promo_list_view(request):
    if request.method == "POST":
        if 'promo_id' in request.POST:
            promo_id = request.POST.get('promo_id')
            try:
                promo = PromoCode.objects.get(id=promo_id)
                promo.delete()
                messages.success(request, f"Промокод {promo.code} успешно удалён.")
            except PromoCode.DoesNotExist:
                messages.error(request, "Промокод не найден.")
            return redirect('promo_list')

        else:
            form = PromoCodeForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                form.save()
                messages.success(request, "Промокод успешно создан.")
                return redirect('promo_list')
            else:
                messages.error(request, "Ошибка при создании промокода.")
    else:
        form = PromoCodeForm()

    today = timezone.now().date()
    promos = PromoCode.objects.filter(is_active=True, valid_from__lte=today)

    return render(request, 'products/promo_list.html', {
        'promos': promos,
        'form': form,
    })
