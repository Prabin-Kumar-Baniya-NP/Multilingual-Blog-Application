from rest_framework.permissions import BasePermission

class AuthorOnly(BasePermission):
    message = "You don't have permission to edit this post"

    def has_object_permission(self, request, view, obj):
        return obj.author.id == request.user.id