from django.contrib.auth.models import Group
from rest_framework import permissions

import logging
logger = logging.getLogger(__name__)


def is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


def has_group_permission(user, required_groups):
    return any([is_in_group(user, group_name) for group_name in required_groups])


class IsEmployee(permissions.BasePermission):
    required_groups = ['EMPLOYEE']

    def has_permission(self, request, view):
        _has_group_permission = has_group_permission(request.user, self.required_groups)
        return request.user and _has_group_permission


class IsAdminUser(permissions.BasePermission):
    required_groups = ['ADMIN']

    def has_permission(self, request, view):
        logger.info("has_permission")
        _has_group_permission = has_group_permission(request.user, self.required_groups)
        return request.user and _has_group_permission
    

class IsHumanResource(permissions.BasePermission):
    required_groups = ['HUMAN_RESOURCE']

    def has_permission(self, request, view):
        logger.info("has_permission")
        _has_group_permission = has_group_permission(request.user, self.required_groups)
        return request.user and _has_group_permission


class IsAdminOrHumanResource(permissions.BasePermission):
    required_groups = ['ADMIN', 'HUMAN_RESOURCE']

    def has_permission(self, request, view):
        _has_group_permission = has_group_permission(request.user, self.required_groups)
        return request.user and _has_group_permission
