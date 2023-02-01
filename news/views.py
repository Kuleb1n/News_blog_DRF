from rest_framework.response import Response
from rest_framework.views import APIView
from .models import News
from .serializers import NewsSerializer


class NewsAPIView(APIView):

    def get(self, request):
        news = News.objects.all()
        return Response({'post': NewsSerializer(news, many=True).data})

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'new_news': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'Error': 'Method PUT not allowed.'})
        try:
            instance = News.objects.get(pk=pk)
        except:
            return Response({'Error': 'Object does not exists.'})

        serializer = NewsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'updated news': serializer.data})
