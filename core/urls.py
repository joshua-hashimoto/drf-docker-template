from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


def api_url(version: int = 1, path: str = ''):
    base_url = f'api/v{version}'
    if path:
        return f'{base_url}/{path}/'
    return base_url + '/'


urlpatterns = [
    # django admin
    path('headquarters/', admin.site.urls),
    # third party
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path(api_url('auth/registration'), include('dj_rest_auth.registration.urls')),
    path(api_url('auth'), include('dj_rest_auth.urls')),
    # local apps
    path(api_url(), include('page_api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
