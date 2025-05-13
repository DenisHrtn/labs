from django.urls import path
from .views.products import product_list
from .views.make_order import make_order
from .views.most_popular_products import most_popular_products_view
from .views.unpopular_products import unpopular_products_view
from .views.price_list import price_list_view
from .views.monthly_sales_by_category import monthly_sales_by_category_view
from .views.yearly_revenue_report import yearly_revenue_report_view
from .views.client_sales_summary import client_sales_summary

urlpatterns = [
    path('', product_list, name='product_list'),
    path('order/', make_order, name='make_order'),
    path('most-popular/', most_popular_products_view, name='most_popular_products'),
    path('unpopular/', unpopular_products_view, name='unpopular_products'),
    path('price-list/', price_list_view, name='price_list'),
    path('monthly-sales/', monthly_sales_by_category_view, name='monthly_sales'),
    path('yearly-revenue/', yearly_revenue_report_view, name='yearly_revenue'),
    path('client-sales/', client_sales_summary, name='client_sales'),
]