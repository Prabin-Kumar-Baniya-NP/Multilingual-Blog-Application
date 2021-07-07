from django.db import models
from post.models import Post
from django.contrib.auth.models import User


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    commented_by = models.CharField(max_length=150)

    def __str__(self):
        return self.body
