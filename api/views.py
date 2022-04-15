from django.db.models import query
from django.shortcuts import render, HttpResponse
from rest_framework.serializers import Serializer
from .models import Category, Article
from .serializers import CategorySerializer, ArticleSerializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, SAFE_METHODS, BasePermission


# Create your views here.
class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['category']
    # filterset_fields = ['category']
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [IsAuthenticatedOrReadOnly]


# class ArticleCategory(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['category']
#     # filterset_fields = ['category']
