from rest_framework import generics
from post.models import Post
from post.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from post.permissions import AuthorOnly

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes =  [IsAuthenticated]

class PostListView(generics.ListAPIView):
    queryset = Post.objects.filter(status="A")
    serializer_class = PostSerializer

class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.filter(status="A")
    serializer_class = PostSerializer

class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, AuthorOnly]

class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes =  [IsAuthenticated, AuthorOnly]