from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование компании")
    website = models.URLField(blank=True, null=True, verbose_name="Сайт компании")
    logo = models.ImageField(upload_to='partner_logos/', blank=True, null=True, verbose_name="Логотип")

    def __str__(self):
        return self.name



