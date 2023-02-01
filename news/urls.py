from django.urls import path
from .views import *

urlpatterns = [path('api/v1/news', NewsAPIView.as_view()),
               path('api/v1/news/<int:pk>/', NewsAPIView.as_view()),
               ]
