from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Category, Article
from django.conf import settings


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        Model = Category
        fields = ['name', 'parent', 'slug']

    def get_fields(self):
        fields = super().get_fields()
        fields['children'] = CategorySerializer(many=True, read_only=True)
        return fields


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'category', 'id', 'image', 'title', 'description', 'storie',
            'created_date', 'author', 'storie_positions', 'status'
        ]


class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}
