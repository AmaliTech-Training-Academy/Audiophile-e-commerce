from rest_framework.permissions import BasePermission

class CanDeleteProduct(BasePermission):
    def has_permission(self, request, view):
        # Add your custom permission logic here
        # For example, allow only authenticated users to delete
        return request.user.is_authenticated and request.method == 'DELETE'
