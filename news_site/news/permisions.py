from rest_framework import permissions


class NoAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        return False
