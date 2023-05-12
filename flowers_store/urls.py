from django.urls import path

from .views import get_sellers_info

urlpatterns = [
    path('', get_sellers_info, name='home')
]
