from django.shortcuts import render
from products.models import Vacancy


def vacancy_list_view(request):
    vacancies = Vacancy.objects.order_by('-published_at')
    return render(request, 'products/vacancy_list.html', {'vacancies': vacancies})
