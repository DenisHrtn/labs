from django.shortcuts import render, get_object_or_404, redirect
from products.models import Vacancy
from products.forms.vacancy_form import VacancyForm


def vacancy_edit_view(request, pk):
    if not request.user.is_staff:
        return redirect('vacancy_list')

    vacancy = get_object_or_404(Vacancy, pk=pk)

    if request.method == 'POST':
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = VacancyForm(instance=vacancy)

    return render(request, 'products/vacancy_edit.html', {'form': form, 'vacancy': vacancy})
