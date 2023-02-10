from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import News, Category
from .permissions import IsUserOrReadOnly
from .serializers import NewsSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = LargeResultsSetPagination

    @action(methods=['get'], detail=False)
    def categories(self, request):
        category = Category.objects.all()
        return Response({'categories': [category.category_name for category in category]})

    @action(methods=['get'], detail=True)
    def category(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            return Response({'category': category.category_name})
        except:
            return Response({'Error': f'There is no category with such a key: {pk}'})
