from django.urls import path
from .views.products import product_list
from .views.make_order import make_order
from .views.most_popular_products import most_popular_products_view
from .views.unpopular_products import unpopular_products_view
from .views.price_list import price_list_view
from .views.monthly_sales_by_category import monthly_sales_by_category_view
from .views.yearly_revenue_report import yearly_revenue_report_view
from .views.client_sales_summary import client_sales_summary
from .views.review import product_reviews_view
from .views.promo import promo_list_view
from .views.order_delete import all_orders_view, delete_order_view
from .views.search_product import search_products_view
from .views.vacancy import vacancy_list_view
from .views.news import news_list
from .views.news_detail import news_detail
from .views.faq_view import faq_view
from .views.vacancy_edit_view import vacancy_edit_view
from .views.customers_contacts import customer_contacts_view

urlpatterns = [
    path('', product_list, name='product_list'),
    path('order/', make_order, name='make_order'),
    path('most-popular/', most_popular_products_view, name='most_popular_products'),
    path('unpopular/', unpopular_products_view, name='unpopular_products'),
    path('price-list/', price_list_view, name='price_list'),
    path('monthly-sales/', monthly_sales_by_category_view, name='monthly_sales'),
    path('yearly-revenue/', yearly_revenue_report_view, name='yearly_revenue'),
    path('client-sales/', client_sales_summary, name='client_sales'),
    path('reviews/', product_reviews_view, name='product_reviews'),
    path('promo/', promo_list_view, name='promo_list'),
    path('orders/', all_orders_view, name='all_orders'),
    path('orders/delete/<int:order_id>/', delete_order_view, name='delete_order'),
    path('products/search/', search_products_view, name='search_products'),
    path('vacancies/', vacancy_list_view, name='vacancy_list'),
    path('news/', news_list, name='news_list'),
    path('news/<int:pk>/', news_detail, name='news_detail'),
    path('faq/', faq_view, name='faq'),
    path('vacancies/<int:pk>/edit/', vacancy_edit_view, name='vacancy_edit'),
    path('customer-contacts/', customer_contacts_view, name='customer_contacts'),
]