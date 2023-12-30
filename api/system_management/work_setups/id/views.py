# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Permissions
from domain.user.permissions.groups import IsAdmin

# Serializers
from .serializers import ReadWorkSetupSerializer, \
    UpdateWorkSetupSerializer, DeleteWorkSetupSerializer

# Services
from domain.system.services.work_setup import get_work_setup_by_id, delete_work_setup, update_work_setup

# Django Shortcuts
from django.shortcuts import get_object_or_404
from django.http import Http404

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class WorkSetupsIdAPIView(APIView):

    permission_classes = (IsAdmin,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadWorkSetupSerializer()
        },
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="work_setup_read",
        tags=["system-management.work-setups.id"],
    )
    def get(request, work_setup_id=None):
        logger.info(f"authenticated: {request.user}")
        work_setup = get_work_setup_by_id(work_setup_id)
        if work_setup is None:
            raise Http404
        work_setup_serializer = ReadWorkSetupSerializer(work_setup)
        return Response(work_setup_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="work_setup_delete",
        tags=["system-management.work-setups.id"],
        responses={
            200: DeleteWorkSetupSerializer()
        }
    )
    def delete(request, work_setup_id=None):
        logger.info(f"authenticated: {request.user}")
        work_setup = get_work_setup_by_id(work_setup_id)
        if work_setup is None:
            raise Http404
        # Copy work_setup so that we can return this data from our delete response
        response = {
            'operation': 'delete',
            'domain': 'system',
            'model': 'WorkSetup',
            'data': work_setup
        }
        response_serializer = DeleteWorkSetupSerializer(response)
        response_serializer_data = response_serializer.data

        delete_work_setup(work_setup)

        return Response(response_serializer_data)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="work_setup_update",
        tags=["system-management.work-setups.id"],
        request_body=UpdateWorkSetupSerializer,
        responses={
            200: ReadWorkSetupSerializer()
        }
    )
    def put(request, work_setup_id=None):
        logger.info(f"authenticated: {request.user}")

        work_setup = get_work_setup_by_id(work_setup_id)

        if work_setup is None:
            raise Http404

        work_setup_serializer = UpdateWorkSetupSerializer(
            data=request.data
        )

        work_setup_serializer.is_valid(raise_exception=True)

        update_work_setup(
            work_setup,
            work_setup_serializer.validated_data.get('work_setup', work_setup.work_setup)
        )
        # NOTE: Re-serialize to fetch more detailed data
        work_setup_serializer = ReadWorkSetupSerializer(
            work_setup
        )
        return Response(work_setup_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="work_setup_patch",
        tags=["system-management.work-setups.id"],
        request_body=UpdateWorkSetupSerializer,
        responses={
            200: ReadWorkSetupSerializer()
        }
    )
    def patch(request, work_setup_id=None):
        logger.info(f"authenticated: {request.user}")

        work_setup = get_work_setup_by_id(work_setup_id)
        if work_setup is None:
            raise Http404

        work_setup_serializer = UpdateWorkSetupSerializer(
            data=request.data,
            partial=True
        )
        work_setup_serializer.is_valid(raise_exception=True)

        update_work_setup(
            work_setup,
            work_setup_serializer.validated_data.get('work_setup', work_setup.work_setup)
        )
        # NOTE: Re-serialize to fetch more detailed data
        work_setup_serializer = ReadWorkSetupSerializer(work_setup)
        return Response(work_setup_serializer.data)
