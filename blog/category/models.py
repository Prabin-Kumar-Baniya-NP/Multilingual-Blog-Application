from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=24)
    description = models.TextField(max_length=126)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name