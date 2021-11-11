from rest_framework.permissions import BasePermission

class CommentModifyPermission(BasePermission):
    """
    Permission for user to update/delete their comment
    """
    def has_object_permission(self, request, view, obj):
        if obj.commented_by.id == request.user.id or obj.post.author.id == request.user.id:
            return True
        else:
            return False