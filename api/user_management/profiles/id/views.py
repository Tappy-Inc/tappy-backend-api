from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ReadProfileSerializer, UpdateProfileSerializer, DeleteProfileSerializer
from domain.user.services.profile import get_profile_by_id, delete_profile, update_profile

from django.shortcuts import get_object_or_404
from django.http import Http404

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class ProfileIdAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadProfileSerializer()
        },
        operation_description="description",
        operation_id="profiles_read",
        tags=["user-management.profiles.id"],
    )
    def get(request, profile_id=None):
        logger.info(f"authenticated: {request.user}")
        profile = get_profile_by_id(profile_id)
        if profile is None:
            raise Http404
        profile_serializer = ReadProfileSerializer(profile)
        return Response(profile_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="profiles_delete",
        tags=["user-management.profiles.id"],
        responses={
            200: DeleteProfileSerializer()
        }
    )
    def delete(request, profile_id=None):
        logger.info(f"authenticated: {request.user}")
        profile = get_profile_by_id(profile_id)
        if profile is None:
            raise Http404
        response = {
            'operation': 'delete',
            'domain': 'user_management',
            'model': 'Profile',
            'data': profile
        }
        response_serializer = DeleteProfileSerializer(response)
        response_serializer_data = response_serializer.data

        delete_profile(profile)

        return Response(response_serializer_data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="profiles_update",
        tags=["user-management.profiles.id"],
        request_body=UpdateProfileSerializer,
        responses={
            200: ReadProfileSerializer()
        }
    )
    def put(request, profile_id=None):
        logger.info(f"authenticated: {request.user}")

        profile = get_profile_by_id(profile_id)

        if profile is None:
            raise Http404

        profile_serializer = UpdateProfileSerializer(
            data=request.data
        )

        profile_serializer.is_valid(raise_exception=True)

        update_profile(
            profile,
            profile_serializer.validated_data.get('bio', profile.bio),
            profile_serializer.validated_data.get('location', profile.location),
            profile_serializer.validated_data.get('gender', profile.gender),
            profile_serializer.validated_data.get('civil_status', profile.civil_status),
            profile_serializer.validated_data.get('employee_id', profile.employee_id),
            profile_serializer.validated_data.get('birth_date', profile.birth_date),
            profile_serializer.validated_data.get('manager', profile.manager)
        )
        profile_serializer = ReadProfileSerializer(profile)
        return Response(profile_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="profiles_patch",
        tags=["user-management.profiles.id"],
        request_body=UpdateProfileSerializer,
        responses={
            200: ReadProfileSerializer()
        }
    )
    def patch(request, profile_id=None):
        logger.info(f"authenticated: {request.user}")

        profile = get_profile_by_id(profile_id)
        if profile is None:
            raise Http404

        profile_serializer = UpdateProfileSerializer(
            data=request.data,
            partial=True
        )
        profile_serializer.is_valid(raise_exception=True)

        update_profile(
            profile,
            profile_serializer.validated_data.get('bio', profile.bio),
            profile_serializer.validated_data.get('location', profile.location),
            profile_serializer.validated_data.get('gender', profile.gender),
            profile_serializer.validated_data.get('civil_status', profile.civil_status),
            profile_serializer.validated_data.get('employee_id', profile.employee_id),
            profile_serializer.validated_data.get('birth_date', profile.birth_date),
            profile_serializer.validated_data.get('manager', profile.manager)
        )
        profile_serializer = ReadProfileSerializer(profile)
        return Response(profile_serializer.data)
