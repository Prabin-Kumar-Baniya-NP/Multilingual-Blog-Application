from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=24, unique=True)
    description = models.TextField(max_length=126, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=48, default="None")

    def __str__(self):
        return self.name