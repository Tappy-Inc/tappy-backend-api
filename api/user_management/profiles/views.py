from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Permissions
from domain.user.permissions.groups import IsAdminOrHumanResource

# Serializers
from .serializers import ReadProfileSerializer, \
    CreateProfileSerializer, PaginateReadProfileSerializer, \
    PaginateQueryReadProfileSerializer

# Services
from domain.user.services.profile import get_profiles, create_profile

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class ProfilesAPIView(APIView):

    permission_classes = (IsAdminOrHumanResource,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadProfileSerializer()
        },
        operation_id="profiles_list",
        tags=["user-management.profiles"],
        query_serializer=PaginateQueryReadProfileSerializer()
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        profiles = get_profiles()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(profiles, request)
        profile_serializer = ReadProfileSerializer(result_page, many=True)
        return paginator.get_paginated_response(profile_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateProfileSerializer,
        operation_description="description",
        operation_id="profiles_create",
        tags=["user-management.profiles"],
        responses={
            200: ReadProfileSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        profile_serializer = CreateProfileSerializer(data=request.data)
        profile_serializer.is_valid(raise_exception=True)

        profile = create_profile(
            user=profile_serializer.validated_data['user'], 
            bio=profile_serializer.validated_data['bio'], 
            location=profile_serializer.validated_data['location'],  
            gender=profile_serializer.validated_data['gender'], 
            civil_status=profile_serializer.validated_data['civil_status'], 
            employee_id=profile_serializer.validated_data['employee_id'], 
            birth_date=profile_serializer.validated_data['birth_date'], 
            manager=profile_serializer.validated_data['manager']
        )
        profile_serializer = ReadProfileSerializer(profile)
        return Response(profile_serializer.data)
