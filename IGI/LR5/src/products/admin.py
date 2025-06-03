from django.contrib import admin
from .models import News
from users.models import Customer


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    fields = ('title', 'content', 'image')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')
