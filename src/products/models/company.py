from django.db import models


class AboutCompany(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название компании")
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True, verbose_name="Логотип")
    description = models.TextField(verbose_name="Информация о компании")
    video_url = models.URLField(blank=True, null=True, verbose_name="Видео")
    requisites = models.TextField(blank=True, verbose_name="Реквизиты")
    certificate_text = models.TextField(blank=True, verbose_name="Сертификат")

    def __str__(self):
        return self.name


class CompanyHistory(models.Model):
    company = models.ForeignKey(AboutCompany, on_delete=models.CASCADE, related_name='history')
    year = models.PositiveIntegerField()
    event = models.TextField()

    class Meta:
        ordering = ["-year"]

    def __str__(self):
        return f"{self.year}: {self.event[:30]}"



