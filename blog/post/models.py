from django.db import models
from category.models import Category
from django.contrib.auth.models import User
from django.dispatch import receiver
import os

class Post(models.Model):
    title = models.CharField(max_length=126)
    image = models.ImageField(upload_to = "postImages/", null = True, blank = True)
    body = models.TextField(max_length=1000, default="None")
    published_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

@receiver(models.signals.pre_save, sender=Post)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes the old image of Post whenever user updates the post object image.
    """
    if not instance.pk:
        return False

    try:
        old_image = Post.objects.get(pk=instance.pk).image
    except Post.DoesNotExist:
        return False

    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)

@receiver(models.signals.post_delete, sender=Post)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes image of Post when the corresponding post is deleted
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)