from django.db import models

from common_services.mixins.audit_mixin import AuditMixin


class ProductCategory(AuditMixin):
    name = models.CharField(max_length=100, verbose_name="Вид мебели")
