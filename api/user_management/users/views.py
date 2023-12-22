# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Permissions
from domain.user.permissions.groups import IsAdminOrHumanResource

# Serializers
from .serializers import ReadUserSerializer, \
    CreateUserSerializer, PaginateReadUserSerializer, \
    PaginateQueryReadUserSerializer

# Services
from domain.common.services.resend import send_email
from domain.user.services.user import get_users, create_user


# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class UsersAPIView(APIView):

    permission_classes = (IsAdminOrHumanResource,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadUserSerializer()
        },
        operation_id="users_list",
        tags=["user-management.users"],
        query_serializer=PaginateQueryReadUserSerializer()
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        users = get_users()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(users, request)
        user_serializer = ReadUserSerializer(result_page, many=True)
        return paginator.get_paginated_response(user_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateUserSerializer,
        operation_description="description",
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

        send_email(
            to=[user.email],
            subject="Welcome to Tappy Inc.!",
            html="""
            <html>
            <body>
            <h1>Welcome to Tappy Inc.!</h1>
            <p>We are thrilled to have you on board. At Tappy Inc., we believe in creating a collaborative and innovative environment where every member can contribute their unique skills and perspectives.</p>
            <p>We are confident that you will bring great value to our team and we look forward to the amazing things we will achieve together.</p>
            <p>Once again, welcome to the team!</p>
            <p>Best,</p>
            <p>The Tappy Inc. Team</p>
            </body>
            </html>
            """
        )
        
        return Response(user_serializer.data)
