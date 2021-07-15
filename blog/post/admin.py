from django.contrib import admin
from django.contrib.admin.decorators import action
from post.models import Post
from django.contrib.auth.models import Group
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

class PostAdmin(admin.ModelAdmin):
    exclude = ("status",)
    list_display = ("title", "author", "status", "published_on")
    list_filter = ("status", "published_on")
    search_fields = ("title", "author__username")
    actions = (approve, reject, block, set_pending)


admin.site.register(Post, PostAdmin)
admin.site.unregister(Group)

admin.site.site_header = "Prabin Kumar Baniya"
admin.site.site_title = "Prabin Kumar Baniya"

admin.site.enable_nav_sidebar = False

