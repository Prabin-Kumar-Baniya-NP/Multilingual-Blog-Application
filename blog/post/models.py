from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=126)
    body = models.TextField(max_length=1000)
    published_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title