from django.contrib import admin
from category.models import Category
from django.contrib import messages

    
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("status",)
    list_display = ("name", "status", "created_by", "created_on")
    list_filter = ("status", "created_on")

admin.site.register(Category, CategoryAdmin)