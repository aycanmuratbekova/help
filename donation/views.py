# import APIView as APIView
from rest_framework import generics, status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer, ArticleSerializer
from .models import Article, Category
from rest_framework.decorators import api_view
from rest_framework import viewsets


class CategoryAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ArticleAPIView(generics.ListAPIView):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def get(self, category_id, **kwargs):
        queryset = Article.objects.filter(id=category_id)
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)






