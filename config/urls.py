"""
URL configuration for career compass project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from career.views import assessment, end_session, home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("assessment/", assessment, name="assessment"),
    path("logout/", end_session, name="end_session"),
    path("", home, name="home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Career Compass Admin"
admin.site.index_title = "Career Compass Admin"
admin.site.site_title = "Career Compass Administration"
