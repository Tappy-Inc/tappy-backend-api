# Django
from django.db.models import Q

# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Permissions
from domain.user.permissions.groups import IsAdminOrHumanResource

# Serializers
from .serializers import ReadUserSerializer, \
    CreateUserSerializer, PaginateReadUserSerializer, \
    PaginateQueryReadUserSerializer

# Services
from domain.user.services.user import get_users, create_user

# Library: django-filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Filters
from domain.user.filters.users import UserFilter

# Memphis
from asgiref.sync import async_to_sync
from domain.memphis.services.producer import create_message

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class UsersAPIView(ListAPIView):

    permission_classes = (IsAdminOrHumanResource,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = UserFilter
    search_fields = ['username', 'email', 'first_name', 'last_name', 'middle_name', 'profile__employee_id']
    ordering_fields = ['id', 'username']
    serializer_class = ReadUserSerializer
<<<<<<< HEAD
    # NOTE: To not being called during Django initialization need to be called in the get_queryset method
    # queryset would only work directly on objects
    # queryset = get_users()
    # NOTE: To use pagination instead of Limit and Offset
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return get_users()
=======
    queryset = get_users()
>>>>>>> 86ee6dc (feat: search and filters)

    @swagger_auto_schema(
        responses={
            200: PaginateReadUserSerializer()
        },
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="users_list",
        tags=["user-management.users"],
        # NOTE: To use pagination instead of Limit and Offset (comment out the next line)
        #       This will be override by the ListAPIView and it's classes
        # query_serializer=PaginateQueryReadUserSerializer()
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateUserSerializer,
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="users_create",
        tags=["user-management.users"],
        responses={
            200: ReadUserSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        user_serializer = CreateUserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = create_user(user_serializer.validated_data['username'], user_serializer.validated_data['password'], user_serializer.validated_data['first_name'], user_serializer.validated_data['last_name'], user_serializer.validated_data['email'])
        user_serializer = ReadUserSerializer(user)

        message = {
            "event": "user_created",
            "data": {
                "user_id": user.id
            }
        }

        async_to_sync(create_message)(message)

        return Response(user_serializer.data)
