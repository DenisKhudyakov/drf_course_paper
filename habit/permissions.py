from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsOwner(permissions.BasePermission):
    """Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD."""

    def has_object_permission(self, request, view, obj):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        return obj.creator == request.user


class IsPublic(permissions.BasePermission):
    """Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять."""

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return obj.is_public
