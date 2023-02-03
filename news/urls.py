from django.urls import path
from .views import *

urlpatterns = [path('api/v1/news', NewsAPIView.as_view()),
               path('api/v1/news/<int:pk>/', NewsUpdateAPIView.as_view()),
               path('api/v1/news-detail/<int:pk>/', NewsDetailAPIView.as_view()),
               ]
