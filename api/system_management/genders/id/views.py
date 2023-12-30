# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Permissions
from domain.user.permissions.groups import IsAdmin

# Serializers
from .serializers import ReadGenderSerializer, \
    UpdateGenderSerializer, DeleteGenderSerializer

# Services
from domain.system.services.gender import get_gender_by_id, delete_gender, update_gender

# Django Shortcuts
from django.shortcuts import get_object_or_404
from django.http import Http404

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class GendersIdAPIView(APIView):

    permission_classes = (IsAdmin,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadGenderSerializer()
        },
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="genders_read",
        tags=["system-management.genders.id"],
    )
    def get(request, gender_id=None):
        logger.info(f"authenticated: {request.user}")
        gender = get_gender_by_id(gender_id)
        if gender is None:
            raise Http404
        gender_serializer = ReadGenderSerializer(gender)
        return Response(gender_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="genders_delete",
        tags=["system-management.genders.id"],
        responses={
            200: DeleteGenderSerializer()
        }
    )
    def delete(request, gender_id=None):
        logger.info(f"authenticated: {request.user}")
        gender = get_gender_by_id(gender_id)
        if gender is None:
            raise Http404
        # Copy gender so that we can return this data from our delete response
        response = {
            'operation': 'delete',
            'domain': 'system',
            'model': 'Gender',
            'data': gender
        }
        response_serializer = DeleteGenderSerializer(response)
        response_serializer_data = response_serializer.data

        delete_gender(gender)

        return Response(response_serializer_data)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="genders_update",
        tags=["system-management.genders.id"],
        request_body=UpdateGenderSerializer,
        responses={
            200: ReadGenderSerializer()
        }
    )
    def put(request, gender_id=None):
        logger.info(f"authenticated: {request.user}")

        gender = get_gender_by_id(gender_id)

        if gender is None:
            raise Http404

        gender_serializer = UpdateGenderSerializer(
            data=request.data
        )

        gender_serializer.is_valid(raise_exception=True)

        update_gender(
            gender,
            gender_serializer.validated_data.get('gender', gender.gender)
        )
        # NOTE: Re-serialize to fetch more detailed data
        gender_serializer = ReadGenderSerializer(
            gender
        )
        return Response(gender_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="genders_patch",
        tags=["system-management.genders.id"],
        request_body=UpdateGenderSerializer,
        responses={
            200: ReadGenderSerializer()
        }
    )
    def patch(request, gender_id=None):
        logger.info(f"authenticated: {request.user}")

        gender = get_gender_by_id(gender_id)
        if gender is None:
            raise Http404

        gender_serializer = UpdateGenderSerializer(
            data=request.data,
            partial=True
        )
        gender_serializer.is_valid(raise_exception=True)

        update_gender(
            gender,
            gender_serializer.validated_data.get('gender', gender.gender)
        )
        # NOTE: Re-serialize to fetch more detailed data
        gender_serializer = ReadGenderSerializer(gender)
        return Response(gender_serializer.data)
