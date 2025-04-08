from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """
    Custom permission to allow only the author of a ToDo to access or modify it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is the author of the ToDo
        return obj.author == request.user
