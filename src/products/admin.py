from django.contrib import admin
from .models import News
from .models.partner import Partner
from .models.company import AboutCompany, CompanyHistory
from users.models import Customer


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    fields = ('title', 'content', 'image')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    fields = ('name', 'website', 'logo')


class CompanyHistoryInline(admin.TabularInline):
    model = CompanyHistory
    extra = 1


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name', 'logo', 'description', 'video_url', 'requisites', 'certificate_text')
    inlines = [CompanyHistoryInline]
