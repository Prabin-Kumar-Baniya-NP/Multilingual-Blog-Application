from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    CATEGORY_STATUS_CHOICES = [
        ('P', "Pending For Approval"),
        ('R', "Rejected"),
        ('A', "Approved"),
        ('B', "Blocked"),
    ]
    name = models.CharField(_("Category Name"), max_length=24, unique=True)
    description = models.TextField(_("Category Description"), max_length=126, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_("Created On"))
    updated_on = models.DateTimeField(auto_now=True, verbose_name = _("Last Updated On"))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = _("Created By"))
    status = models.CharField(_("Category Status"), max_length=1, choices=CATEGORY_STATUS_CHOICES, default='P')

    class Meta:
        db_table = "Category"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name