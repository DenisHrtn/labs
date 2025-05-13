from django.db import models

from common_services.mixins.audit_mixin import AuditMixin
from common_services.utils.generate_product_code import generate_random_product_code
from .product_category import ProductCategory
from .product_model import ProductModel


class Product(AuditMixin):
    name = models.CharField(max_length=255, verbose_name="Название изделия")
    product_code = models.IntegerField(default=generate_random_product_code)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="Категория")
    model = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name="Модель")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    is_active = models.BooleanField(default=True, verbose_name="В производстве")
