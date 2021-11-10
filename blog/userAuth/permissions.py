from rest_framework.permissions import BasePermission

class HasObjectOwnership(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id != obj.id:
            return False
        return super().has_object_permission(request, view, obj)