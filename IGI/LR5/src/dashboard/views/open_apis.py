import requests
from django.shortcuts import render


def cat_fact_view(request):
    try:
        response = requests.get('https://catfact.ninja/fact')
        response.raise_for_status()
        fact = response.json().get('fact')
    except requests.RequestException:
        fact = None
    return render(request, 'dashboard/cat_fact.html', {'fact': fact})


def nationalize_view(request):
    name = request.GET.get('name')
    countries = []

    if name:
        try:
            response = requests.get('https://api.nationalize.io/', params={'name': name})
            response.raise_for_status()
            countries = response.json().get('country', [])
        except requests.RequestException:
            countries = []

    return render(request, 'dashboard/nationalize.html', {
        'name': name,
        'countries': countries
    })
