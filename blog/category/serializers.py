from django.contrib.auth import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from category.models import Category
from rest_framework.exceptions import ValidationError

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["created_on", "updated_on"]

    def validate(self, attrs):
        if self.context["request"].user.id != attrs["created_by"].id:
            raise ValidationError(detail="created_by value must be equal to user id")
        return super().validate(attrs)

class CategorySerializerForPost(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
