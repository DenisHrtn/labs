from django.db import models

from common_services.mixins.audit_mixin import AuditMixin
from .order import Order
from .product import Product


class OrderItem(AuditMixin):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
