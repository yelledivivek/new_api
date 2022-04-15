from api.models import Article
from django.db import router
from django.urls import path, include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
# router.register('category', ArticleCategory, basename='category')

urlpatterns = [
    path('api/', include(router.urls)),

]
