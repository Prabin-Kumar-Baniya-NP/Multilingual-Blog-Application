from rest_framework.generics import ListAPIView
from category.models import Category
from post.models import Post
from category.serializers import CategorySerializer
from post.serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination


class AuthorCategoryListView(ListAPIView):
    """
    Lists the categories created by specific author
    For auther : it returns all categories
    For non-author: it returns only approved categories
    """
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        if self.request.user.id == self.kwargs["pk"]:
            return Category.objects.filter(created_by = self.kwargs["pk"])
        else:
            return Category.objects.filter(status="A", created_by = self.kwargs["pk"])

class AuthorPostsListView(ListAPIView):
    """
    Lists the posts created by specific author
    For auther : it returns all posts
    For non-author: it returns only approved posts
    """
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        if self.request.user.id == self.kwargs["pk"]:
            return Post.objects.filter(author=self.kwargs["pk"])
        else:
            return Post.objects.filter(status="A", author=self.kwargs["pk"])
