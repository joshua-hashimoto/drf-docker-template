from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # django admin
    path('headquarters/', admin.site.urls),
    # third party
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('maintenance-mode/', include('maintenance_mode.urls')),
    # local apps
    path('', include('pages.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
