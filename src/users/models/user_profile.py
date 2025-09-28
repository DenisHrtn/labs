from django.db import models

from common_services.mixins.audit_mixin import AuditMixin
from .user import User


class UserProfile(AuditMixin):
    ROLE_CHOICES = [
        ('staff', 'Сотрудник'),
        ('customer', 'Покупатель'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
