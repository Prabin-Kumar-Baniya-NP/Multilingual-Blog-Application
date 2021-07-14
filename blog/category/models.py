from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    CATEGORY_STATUS_CHOICES = [
        ('P', "Pending For Approval"),
        ('R', "Rejected"),
        ('A', "Approved"),
        ('B', "Blocked"),
    ]
    name = models.CharField("Category Name", max_length=24, unique=True)
    description = models.TextField("Category Description", max_length=126, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created On")
    updated_on = models.DateTimeField(auto_now=True, verbose_name = "Last Updated On")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "Created By")
    status = models.CharField("Category Status", max_length=1, choices=CATEGORY_STATUS_CHOICES, default='P')

    def __str__(self):
        return self.name