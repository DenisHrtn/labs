import os

from django.conf import settings
from django.shortcuts import render
from django.http import FileResponse

from ..models import AboutCompany
from ..models import Partner


def about_view(request):
    company = AboutCompany.objects.first()
    return render(request, 'pages/about.html', {'company': company})


def partners_view(request):
    partners = Partner.objects.all()
    return render(request, 'pages/partners.html', {'partners': partners})


def privacy_view(request):
    return render(request, 'pages/privacy.html')


def download_privacy(request):
    filepath = os.path.join(settings.MEDIA_ROOT, "privacy/forma-nda-konfedicialnost.pdf")
    return FileResponse(open(filepath, "rb"), as_attachment=True, filename="privacy_policy.pdf")


