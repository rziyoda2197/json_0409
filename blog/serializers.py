from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = ["id", "name"]


class PostSerializer(serializers.ModelSerializer):
    # O'qishda kategoriya nomini ham ko'rsatish uchun
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model  = Post
        fields = [
            "id",
            "title",
            "body",
            "category",       # yozishda ID qabul qiladi
            "category_name",  # o'qishda ism qaytaradi
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]