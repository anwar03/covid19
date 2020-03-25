from rest_framework import permissions

from employee.models import Employee

safe_methoeds = ('GET', 'POST', 'HEAD', 'OPTIONS')


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in safe_methoeds and not request.user.is_superuser:
            employee = Employee.objects.get(user=request.user)
            return request.user.is_staff and employee.group.name == "Admin"

    def has_object_permission(self, request, view, obj):
        if request.method in safe_methoeds and not request.user.is_superuser:
            employee = Employee.objects.get(user=request.user)
            return request.user.is_staff and employee.group.name == "Admin"
