from django.urls import path

from .views import PageAPIView

app_name = 'page_api'

urlpatterns = [
    path('', PageAPIView.as_view(), name='default'),
]
