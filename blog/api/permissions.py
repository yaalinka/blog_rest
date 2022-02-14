from rest_framework import permissions


class CustomerAccessPermission(permissions.BasePermission):
    message = "You can not delete someone's article."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
