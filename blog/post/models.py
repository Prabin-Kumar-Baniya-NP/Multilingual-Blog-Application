from django.db import models
from category.models import Category
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    POST_STATUS_CHOICES = [
        ('P', "Pending For Approval"),
        ('R', "Rejected"),
        ('A', "Approved"),
        ('B', "Blocked"),
    ]
    title = models.CharField("Post Title",
                             max_length=126,
                             error_messages={
                                 'max_length':
                                 "Title cann't be more than 126 characters",
                             })
    image = models.ImageField(upload_to="postImages/",
                              null=True,
                              blank=True,
                              default=None,
                              verbose_name="Post Image")
    body = RichTextField("Post Description",
                            max_length=1000,
                            default="None")
    slug = models.SlugField("Slug Field", max_length=250, unique=True, null=True, blank=True)
    published_on = models.DateTimeField("Publication Date", auto_now_add=True)
    last_updated = models.DateTimeField("Last Updated", auto_now=True)
    category = models.ManyToManyField(Category,
                                      blank=True,
                                      verbose_name="Category")
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name="Author Username")
    status = models.CharField("Post Status",
                              max_length=1,
                              choices=POST_STATUS_CHOICES,
                              default='P')

    class Meta:
        db_table = "Post"
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post:view-post', kwargs={'pk': self.slug})