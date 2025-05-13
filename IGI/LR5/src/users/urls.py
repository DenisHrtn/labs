from django.urls import path

from users.views.register import register_view
from users.views.login import login_view
from users.views.logout import logout_view
from users.views.customer_by_city import customers_by_city_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('customers-by-city/', customers_by_city_view, name='customers_by_city'),
]
