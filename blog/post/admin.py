from django.contrib import admin
from post.models import Post
from django.contrib.auth.models import Group
from django.contrib import messages

class PostAdmin(admin.ModelAdmin):
    exclude = ("status",)
    list_display = ("title", "author", "status", "published_on")
    list_filter = ("status", "published_on")
    search_fields = ("title", "author__username")

    def approve(modeladmin, request, queryset):
        queryset.update(status = "A")
        messages.success(request, "Selected Item(s) Approved")
    
    def reject(modeladmin, request, queryset):
        queryset.update(status = "R")
        messages.success(request, "Selected Item(s) Rejected")

    def block(modeladmin, request, queryset):
        queryset.update(status = "B")
        messages.success(request, "Selected Item(s) Blocked")
    
    def set_pending(modeladmin, request, queryset):
        queryset.update(status = "P")
        messages.success(request, "Selected Item(s) is set to Pending for Approval")
    
    admin.site.add_action(approve, "Set as Approved")
    admin.site.add_action(reject, "Set as Rejected")
    admin.site.add_action(block, "Set as Blocked")
    admin.site.add_action(set_pending, "Set as Pending for Approval")

admin.site.register(Post, PostAdmin)
admin.site.unregister(Group)

admin.site.site_header = "Prabin Kumar Baniya"
admin.site.site_title = "Prabin Kumar Baniya"

admin.site.enable_nav_sidebar = False

