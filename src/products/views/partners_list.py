from django.shortcuts import render
from ..models import Partner


def partners_list_view(request):
    """
    Отображает страницу со списком всех партнёров.
    """
    partners = Partner.objects.all()
    context = {
        'partners': partners,
    }
    return render(request, 'pages/partners.html', context)
