from django.db import models

from common_services.mixins.audit_mixin import AuditMixin
from users.models import User


class Customer(AuditMixin):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
