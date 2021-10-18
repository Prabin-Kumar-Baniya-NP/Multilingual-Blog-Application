from django.contrib.auth import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from category.models import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CategorySerializerForPost(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
