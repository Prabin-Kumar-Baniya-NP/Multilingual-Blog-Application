from rest_framework.response import Response
from post.models import Post
from post.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied, ValidationError
from post.pagination import PostPagination
from rest_framework.decorators import api_view
from comment.models import Comment
from comment.serializer import CommentSerializer
from rest_framework.pagination import PageNumberPagination

class PostAPIViewSet(ModelViewSet):
    """
    Viewsets for creating, updating, deleting, retrieving posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.filter(status="A").order_by("-published_on")

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == "A":
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            raise PermissionDenied({"error": "This post is not approved"})
    
    def create(self, request, *args, **kwargs):
        if request.data["author"] != self.request.user.id:
            raise ValidationError({"error": "Author ID doesn't matches with your user id"})
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author.id != request.user.id:
            raise ValidationError({"error": "Only Author Can Update this Post"})
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author.id != request.user.id:
            raise ValidationError({"error": "Only Author Can Delete this Post"})
        return super().destroy(request, *args, **kwargs)

@api_view(["GET"])
def get_comments_by_postID(request, postID):
    posts = Comment.objects.filter(post = postID).order_by("-commented_on")
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(posts, request)
    serializer = CommentSerializer(result_page, many = True)
    return paginator.get_paginated_response(serializer.data)