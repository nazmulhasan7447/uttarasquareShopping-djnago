from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'', include('core.urls')),
    re_path(r'', include('adminPanel.urls')),
    re_path(r'', include('user.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Uttarasquare Adminstration"
admin.site.index_title = 'Site Models'
admin.site.site_title = 'Databse Adminstration'
