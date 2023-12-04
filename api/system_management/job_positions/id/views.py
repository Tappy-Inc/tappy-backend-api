# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Serializers
from .serializers import ReadJobPositionSerializer, \
    UpdateJobPositionSerializer, DeleteJobPositionSerializer

# Services
from domain.system.services.job_position import get_job_position_by_id, delete_job_position, update_job_position

# Django Shortcuts
from django.shortcuts import get_object_or_404
from django.http import Http404

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class JobPositionsIdAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadJobPositionSerializer()
        },
        operation_description="description",
        operation_id="job_positions_read",
        tags=["system-management.job_positions.id"],
    )
    def get(request, job_position_id=None):
        logger.info(f"authenticated: {request.user}")
        job_position = get_job_position_by_id(job_position_id)
        if job_position is None:
            raise Http404
        job_position_serializer = ReadJobPositionSerializer(job_position)
        return Response(job_position_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="job_positions_delete",
        tags=["system-management.job_positions.id"],
        responses={
            200: DeleteJobPositionSerializer()
        }
    )
    def delete(request, job_position_id=None):
        logger.info(f"authenticated: {request.user}")
        job_position = get_job_position_by_id(job_position_id)
        if job_position is None:
            raise Http404
        # Copy job_position so that we can return this data from our delete response
        response = {
            'operation': 'delete',
            'domain': 'system',
            'model': 'JobPosition',
            'data': job_position
        }
        response_serializer = DeleteJobPositionSerializer(response)
        response_serializer_data = response_serializer.data

        delete_job_position(job_position)

        return Response(response_serializer_data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="job_positions_update",
        tags=["system-management.job_positions.id"],
        request_body=UpdateJobPositionSerializer,
        responses={
            200: ReadJobPositionSerializer()
        }
    )
    def put(request, job_position_id=None):
        logger.info(f"authenticated: {request.user}")

        job_position = get_job_position_by_id(job_position_id)

        if job_position is None:
            raise Http404

        job_position_serializer = UpdateJobPositionSerializer(
            data=request.data
        )

        job_position_serializer.is_valid(raise_exception=True)

        update_job_position(
            job_position,
            job_position_serializer.validated_data.get('position_name', job_position.position_name),
            job_position_serializer.validated_data.get('department', job_position.department)
        )
        # NOTE: Re-serialize to fetch more detailed data
        job_position_serializer = ReadJobPositionSerializer(
            job_position
        )
        return Response(job_position_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="job_positions_patch",
        tags=["system-management.job_positions.id"],
        request_body=UpdateJobPositionSerializer,
        responses={
            200: ReadJobPositionSerializer()
        }
    )
    def patch(request, job_position_id=None):
        logger.info(f"authenticated: {request.user}")

        job_position = get_job_position_by_id(job_position_id)
        if job_position is None:
            raise Http404

        job_position_serializer = UpdateJobPositionSerializer(
            data=request.data,
            partial=True
        )
        job_position_serializer.is_valid(raise_exception=True)

        update_job_position(
            job_position,
            job_position_serializer.validated_data.get('position_name', job_position.position_name),
            job_position_serializer.validated_data.get('department', job_position.department)
        )
        # NOTE: Re-serialize to fetch more detailed data
        job_position_serializer = ReadJobPositionSerializer(job_position)
        return Response(job_position_serializer.data)
