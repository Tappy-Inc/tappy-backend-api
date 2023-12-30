# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Permissions
from domain.user.permissions.groups import IsAdmin

# Serializers
from .serializers import ReadEmploymentTypeSerializer, \
    UpdateEmploymentTypeSerializer, DeleteEmploymentTypeSerializer

# Services
from domain.system.services.employment_type import get_employment_type_by_id, delete_employment_type, update_employment_type

# Django Shortcuts
from django.shortcuts import get_object_or_404
from django.http import Http404

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class EmploymentTypesIdAPIView(APIView):

    permission_classes = (IsAdmin,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadEmploymentTypeSerializer()
        },
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="employment_type_read",
        tags=["system-management.employment-types.id"],
    )
    def get(request, employment_type_id=None):
        logger.info(f"authenticated: {request.user}")
        employment_type = get_employment_type_by_id(employment_type_id)
        if employment_type is None:
            raise Http404
        employment_type_serializer = ReadEmploymentTypeSerializer(employment_type)
        return Response(employment_type_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="employment_type_delete",
        tags=["system-management.employment-types.id"],
        responses={
            200: DeleteEmploymentTypeSerializer()
        }
    )
    def delete(request, employment_type_id=None):
        logger.info(f"authenticated: {request.user}")
        employment_type = get_employment_type_by_id(employment_type_id)
        if employment_type is None:
            raise Http404
        # Copy employment_type so that we can return this data from our delete response
        response = {
            'operation': 'delete',
            'domain': 'system',
            'model': 'EmploymentType',
            'data': employment_type
        }
        response_serializer = DeleteEmploymentTypeSerializer(response)
        response_serializer_data = response_serializer.data

        delete_employment_type(employment_type)

        return Response(response_serializer_data)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="employment_type_update",
        tags=["system-management.employment-types.id"],
        request_body=UpdateEmploymentTypeSerializer,
        responses={
            200: ReadEmploymentTypeSerializer()
        }
    )
    def put(request, employment_type_id=None):
        logger.info(f"authenticated: {request.user}")

        employment_type = get_employment_type_by_id(employment_type_id)

        if employment_type is None:
            raise Http404

        employment_type_serializer = UpdateEmploymentTypeSerializer(
            data=request.data
        )

        employment_type_serializer.is_valid(raise_exception=True)

        update_employment_type(
            employment_type,
            employment_type_serializer.validated_data.get('employment_type', employment_type.employment_type)
        )
        # NOTE: Re-serialize to fetch more detailed data
        employment_type_serializer = ReadEmploymentTypeSerializer(
            employment_type
        )
        return Response(employment_type_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="employment_type_patch",
        tags=["system-management.employment-types.id"],
        request_body=UpdateEmploymentTypeSerializer,
        responses={
            200: ReadEmploymentTypeSerializer()
        }
    )
    def patch(request, employment_type_id=None):
        logger.info(f"authenticated: {request.user}")

        employment_type = get_employment_type_by_id(employment_type_id)
        if employment_type is None:
            raise Http404

        employment_type_serializer = UpdateEmploymentTypeSerializer(
            data=request.data,
            partial=True
        )
        employment_type_serializer.is_valid(raise_exception=True)

        update_employment_type(
            employment_type,
            employment_type_serializer.validated_data.get('employment_type', employment_type.employment_type)
        )
        # NOTE: Re-serialize to fetch more detailed data
        employment_type_serializer = ReadEmploymentTypeSerializer(employment_type)
        return Response(employment_type_serializer.data)
