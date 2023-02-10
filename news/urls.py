from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from news.views import NewsViewSet

router = routers.DefaultRouter()

router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
