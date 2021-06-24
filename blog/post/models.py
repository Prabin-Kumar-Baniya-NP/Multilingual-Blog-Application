from django.db import models
from django.utils import tree
from category.models import Category

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=126)
    body = models.TextField(max_length=1000, default="None")
    published_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, blank=True)
    author = models.CharField(max_length=48,default="None")
    likes = models.IntegerField(default=0, null=True, blank=True)
    dislikes = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title