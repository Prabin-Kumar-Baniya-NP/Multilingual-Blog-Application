from django.db import models
from category.models import Category
from django.contrib.auth.models import User


class Post(models.Model):
    POST_STATUS_CHOICES = [
        ('P', "Pending For Approval"),
        ('R', "Rejected"),
        ('A', "Approved"),
        ('B', "Blocked"),
    ]
    title = models.CharField("Post Title", max_length=126)
    image = models.ImageField(upload_to = "postImages/", null = True, blank = True, default = None, verbose_name="Post Image")
    body = models.TextField("Post Description",max_length=1000, default="None")
    published_on = models.DateTimeField("Publication Date", auto_now_add=True)
    last_updated = models.DateTimeField("Last Updated", auto_now=True)
    category = models.ManyToManyField(Category, blank=True, verbose_name="Category")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author Username")
    status = models.CharField("Post Status", max_length=1, choices=POST_STATUS_CHOICES, default='P')

    def __str__(self):
        return self.title