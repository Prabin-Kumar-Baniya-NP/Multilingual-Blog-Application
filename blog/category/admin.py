from django.contrib import admin
from category.models import Category
from django.contrib import messages

@admin.action(description="Mark Selected as Approved")
def approve(modeladmin, request, queryset):
        queryset.update(status = "A")
        messages.success(request, "Selected Item(s) Approved")

@admin.action(description="Mark Selected as Rejected")
def reject(modeladmin, request, queryset):
    queryset.update(status = "R")
    messages.success(request, "Selected Item(s) Rejected")

@admin.action(description="Mark Selected as Blocked")
def block(modeladmin, request, queryset):
    queryset.update(status = "B")
    messages.success(request, "Selected Item(s) Blocked")

@admin.action(description="Mark Selected as Pending for Approval")
def set_pending(modeladmin, request, queryset):
    queryset.update(status = "P")
    messages.success(request, "Selected Item(s) is set to Pending for Approval")

class CategoryAdmin(admin.ModelAdmin):
    exclude = ("status",)
    list_display = ("name", "status", "created_by", "created_on")
    list_filter = ("status", "created_on")
    search_fields = ("name", "created_by__username")
    actions = [approve, reject, block, set_pending]

admin.site.register(Category, CategoryAdmin)