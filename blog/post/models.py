from django.db import models
from category.models import Category
from django.contrib.auth import get_user_model
from django.urls import reverse
import datetime
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

User = get_user_model()
class Post(models.Model):
    POST_STATUS_CHOICES = [
        ('P', "Pending For Approval"),
        ('R', "Rejected"),
        ('A', "Approved"),
        ('B', "Blocked"),
    ]
    title = models.CharField(_("Post Title"),
                             max_length=250,
                             unique=True,
                             error_messages={
                                 'max_length':
                                 "Title cann't be more than 126 characters",
                             })
    image = models.URLField(null=True,
                            blank=True,
                            default=None,
                            verbose_name=_("Post Image URL"))
    body = models.TextField(_("Post Description"),
                            max_length=5000,
                            default="None")
    slug = models.SlugField(_("Slug Field"), max_length=300, unique=True, null=True, blank=True)
    published_on = models.DateTimeField(_("Publication Date"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True)
    category = models.ManyToManyField(Category,
                                      blank=True,
                                      verbose_name="Category")
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name=_("Author Username"))
    status = models.CharField(_("Post Status"),
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
        return reverse('post:view-post', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        def unique_code():
            return str(int(datetime.datetime.now().timestamp() * pow(10, 6)))
        
        if not self.slug:
            self.slug = slugify(str(self.title) + "-" + unique_code())
        return super().save(*args, **kwargs)