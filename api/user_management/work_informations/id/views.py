from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Permissions
from domain.user.permissions.groups import IsAdminOrHumanResource

# Serializers
from .serializers import ReadWorkInformationSerializer, UpdateWorkInformationSerializer, DeleteWorkInformationSerializer

# Services
from domain.user.services.work_information import get_work_information_by_id, delete_work_information, update_work_information

from django.shortcuts import get_object_or_404
from django.http import Http404

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class WorkInformationIdAPIView(APIView):

    permission_classes = (IsAdminOrHumanResource,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadWorkInformationSerializer()
        },
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="work_informations_read",
        tags=["user-management.work-informations.id"],
    )
    def get(request, work_information_id=None):
        logger.info(f"authenticated: {request.user}")
        work_information = get_work_information_by_id(work_information_id)
        if work_information is None:
            raise Http404
        work_information_serializer = ReadWorkInformationSerializer(work_information)
        return Response(work_information_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="work_informations_delete",
        tags=["user-management.work-informations.id"],
        responses={
            200: DeleteWorkInformationSerializer()
        }
    )
    def delete(request, work_information_id=None):
        logger.info(f"authenticated: {request.user}")
        work_information = get_work_information_by_id(work_information_id)
        if work_information is None:
            raise Http404
        response = {
            'operation': 'delete',
            'domain': 'user_management',
            'model': 'WorkInformation',
            'data': work_information
        }
        response_serializer = DeleteWorkInformationSerializer(response)
        response_serializer_data = response_serializer.data

        delete_work_information(work_information)

        return Response(response_serializer_data)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="work_informations_update",
        tags=["user-management.work-informations.id"],
        request_body=UpdateWorkInformationSerializer,
        responses={
            200: ReadWorkInformationSerializer()
        }
    )
    def put(request, work_information_id=None):
        logger.info(f"authenticated: {request.user}")

        work_information = get_work_information_by_id(work_information_id)

        if work_information is None:
            raise Http404

        work_information_serializer = UpdateWorkInformationSerializer(
            data=request.data
        )

        work_information_serializer.is_valid(raise_exception=True)

        update_work_information(
            work_information,
            work_information_serializer.validated_data.get('department', work_information.department),
            work_information_serializer.validated_data.get('job_level', work_information.job_level),
            work_information_serializer.validated_data.get('employment_type', work_information.employment_type),
            work_information_serializer.validated_data.get('work_setup', work_information.work_setup)
        )
        work_information_serializer = ReadWorkInformationSerializer(work_information)
        return Response(work_information_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="work_informations_patch",
        tags=["user-management.work-informations.id"],
        request_body=UpdateWorkInformationSerializer,
        responses={
            200: ReadWorkInformationSerializer()
        }
    )
    def patch(request, work_information_id=None):
        logger.info(f"authenticated: {request.user}")

        work_information = get_work_information_by_id(work_information_id)
        if work_information is None:
            raise Http404

        work_information_serializer = UpdateWorkInformationSerializer(
            data=request.data,
            partial=True
        )
        work_information_serializer.is_valid(raise_exception=True)

        update_work_information(
            work_information,
            work_information_serializer.validated_data.get('department', work_information.department),
            work_information_serializer.validated_data.get('job_level', work_information.job_level),
            work_information_serializer.validated_data.get('employment_type', work_information.employment_type),
            work_information_serializer.validated_data.get('work_setup', work_information.work_setup)
        )
        work_information_serializer = ReadWorkInformationSerializer(work_information)
        return Response(work_information_serializer.data)
