from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Kategoriyalar uchun to'liq CRUD.
    GET    /api/categories/       — ro'yxat
    POST   /api/categories/       — yangi kategoriya
    GET    /api/categories/{id}/  — bitta kategoriya
    PUT    /api/categories/{id}/  — to'liq yangilash
    PATCH  /api/categories/{id}/  — qisman yangilash
    DELETE /api/categories/{id}/  — o'chirish
    """
    queryset         = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends  = [filters.SearchFilter, filters.OrderingFilter]
    search_fields    = ["name"]
    ordering_fields  = ["name"]


class PostViewSet(viewsets.ModelViewSet):
    """
    Maqolalar uchun to'liq CRUD.
    GET    /api/posts/       — ro'yxat
    POST   /api/posts/       — yangi maqola
    GET    /api/posts/{id}/  — bitta maqola
    PUT    /api/posts/{id}/  — to'liq yangilash
    PATCH  /api/posts/{id}/  — qisman yangilash
    DELETE /api/posts/{id}/  — o'chirish
    """
    queryset         = Post.objects.select_related("category").all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends  = [filters.SearchFilter, filters.OrderingFilter]
    search_fields    = ["title", "body", "category__name"]
    ordering_fields  = ["created_at", "updated_at", "title"]