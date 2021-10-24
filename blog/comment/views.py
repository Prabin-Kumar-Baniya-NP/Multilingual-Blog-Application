from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from comment.models import Comment
from comment.serializer import CommentSerializer
from comment.permissions import CommentModifyPermission
from rest_framework.generics import CreateAPIView

class CommentsCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentsModifyAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentModifyPermission]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

