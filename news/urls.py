from django.urls import path, include, re_path
from rest_framework import routers

from news.views import NewsViewSet

router = routers.DefaultRouter()

router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
