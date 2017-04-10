"""
{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/

"""
# Python Imports

# Django Imports
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

# Third Party Django Imports

# Inter App Imports

# Local Imports
from django.conf.urls import url
from django.contrib import admin


admin.site.site_header = admin.site.site_title = '{{ project_name | title }}'


urlpatterns = [
    url(r'^admin/', admin.site.urls),  # Default Admin
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
