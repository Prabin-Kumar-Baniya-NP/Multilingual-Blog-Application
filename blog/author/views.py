from rest_framework.generics import ListAPIView
from category.models import Category
from post.models import Post
from rest_framework.permissions import IsAuthenticated
from category.serializers import CategorySerializer
from post.serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination

class AuthorCategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(created_by = self.kwargs["pk"])

class AuthorPostsListView(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.kwargs["pk"])
