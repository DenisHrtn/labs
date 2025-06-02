from django.urls import path

from .views.dashboard import dashboard_view
from .views.open_apis import cat_fact_view, nationalize_view

urlpatterns = [
    path('dash/', dashboard_view, name='dashboard'),
    path('cat-fact/', cat_fact_view, name='cat_fact'),
    path('nationalize/', nationalize_view, name='nationalize'),
]