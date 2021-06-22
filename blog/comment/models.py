from django.db import models
from post.models import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    commented_by = models.CharField(max_length=48, default="None")

    def __str__(self):
        return self.body
