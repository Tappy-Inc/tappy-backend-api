from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Permissions
from domain.user.permissions.groups import IsAdminOrHumanResource

# Serializers
from .serializers import ReadEducationalBackgroundSerializer, UpdateEducationalBackgroundSerializer, DeleteEducationalBackgroundSerializer

# Services
from domain.user.services.educational_background import get_educational_background_by_id, delete_educational_background, update_educational_background

from django.shortcuts import get_object_or_404
from django.http import Http404

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class EducationalBackgroundIdAPIView(APIView):

    permission_classes = (IsAdminOrHumanResource,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadEducationalBackgroundSerializer()
        },
        operation_description="description",
        operation_id="educational_backgrounds_read",
        tags=["user-management.educational-backgrounds.id"],
    )
    def get(request, educational_background_id=None):
        logger.info(f"authenticated: {request.user}")
        educational_background = get_educational_background_by_id(educational_background_id)
        if educational_background is None:
            raise Http404
        educational_background_serializer = ReadEducationalBackgroundSerializer(educational_background)
        return Response(educational_background_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="educational_backgrounds_delete",
        tags=["user-management.educational-backgrounds.id"],
        responses={
            200: DeleteEducationalBackgroundSerializer()
        }
    )
    def delete(request, educational_background_id=None):
        logger.info(f"authenticated: {request.user}")
        educational_background = get_educational_background_by_id(educational_background_id)
        if educational_background is None:
            raise Http404
        response = {
            'operation': 'delete',
            'domain': 'user_management',
            'model': 'EducationalBackground',
            'data': educational_background
        }
        response_serializer = DeleteEducationalBackgroundSerializer(response)
        response_serializer_data = response_serializer.data

        delete_educational_background(educational_background)

        return Response(response_serializer_data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="educational_backgrounds_update",
        tags=["user-management.educational-backgrounds.id"],
        request_body=UpdateEducationalBackgroundSerializer,
        responses={
            200: ReadEducationalBackgroundSerializer()
        }
    )
    def put(request, educational_background_id=None):
        logger.info(f"authenticated: {request.user}")

        educational_background = get_educational_background_by_id(educational_background_id)

        if educational_background is None:
            raise Http404

        educational_background_serializer = UpdateEducationalBackgroundSerializer(
            data=request.data
        )

        educational_background_serializer.is_valid(raise_exception=True)

        update_educational_background(
            educational_background,
            educational_background_serializer.validated_data.get('education_type', educational_background.education_type),
            educational_background_serializer.validated_data.get('school', educational_background.school),
            educational_background_serializer.validated_data.get('from_year', educational_background.from_year),
            educational_background_serializer.validated_data.get('to_year', educational_background.to_year),
            educational_background_serializer.validated_data.get('degree', educational_background.degree)
        )
        educational_background_serializer = ReadEducationalBackgroundSerializer(educational_background)
        return Response(educational_background_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="educational_backgrounds_patch",
        tags=["user-management.educational-backgrounds.id"],
        request_body=UpdateEducationalBackgroundSerializer,
        responses={
            200: ReadEducationalBackgroundSerializer()
        }
    )
    def patch(request, educational_background_id=None):
        logger.info(f"authenticated: {request.user}")

        educational_background = get_educational_background_by_id(educational_background_id)
        if educational_background is None:
            raise Http404

        educational_background_serializer = UpdateEducationalBackgroundSerializer(
            data=request.data,
            partial=True
        )
        educational_background_serializer.is_valid(raise_exception=True)

        update_educational_background(
            educational_background,
            educational_background_serializer.validated_data.get('education_type', educational_background.education_type),
            educational_background_serializer.validated_data.get('school', educational_background.school),
            educational_background_serializer.validated_data.get('from_year', educational_background.from_year),
            educational_background_serializer.validated_data.get('to_year', educational_background.to_year),
            educational_background_serializer.validated_data.get('degree', educational_background.degree)
        )
        educational_background_serializer = ReadEducationalBackgroundSerializer(educational_background)
        return Response(educational_background_serializer.data)
