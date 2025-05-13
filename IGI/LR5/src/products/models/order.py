from django.db import models

from common_services.mixins.audit_mixin import AuditMixin
from .product import Product
from users.models.customer import Customer


class Order(AuditMixin):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    delivery_date = models.DateField()
    products = models.ManyToManyField(Product, through='OrderItem')
