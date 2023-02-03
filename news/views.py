from rest_framework import generics
from .models import News
from .serializers import NewsSerializer


class NewsAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsUpdateAPIView(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
