from django.urls import path, include
from rest_framework import routers

from news.views import NewsViewSet

router = routers.DefaultRouter()

router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [path('api/v1/', include(router.urls)),
               ]
