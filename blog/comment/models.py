from django.db import models
from post.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Comment"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
    
    def __str__(self):
        return self.body
