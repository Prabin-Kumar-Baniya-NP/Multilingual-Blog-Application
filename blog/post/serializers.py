from rest_framework import serializers
from category.serializers import CategorySerializerForPost
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializerForPost(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = "__all__"