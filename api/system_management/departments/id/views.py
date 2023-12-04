# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Serializers
from .serializers import ReadDepartmentSerializer, \
    UpdateDepartmentSerializer, DeleteDepartmentSerializer

# Services
from domain.system.services.department import get_department_by_id, delete_department, update_department

# Django Shortcuts
from django.shortcuts import get_object_or_404
from django.http import Http404

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class DepartmentsIdAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadDepartmentSerializer()
        },
        operation_description="description",
        operation_id="departments_read",
        tags=["system-management.departments.id"],
    )
    def get(request, department_id=None):
        logger.info(f"authenticated: {request.user}")
        department = get_department_by_id(department_id)
        if department is None:
            raise Http404
        department_serializer = ReadDepartmentSerializer(department)
        return Response(department_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="departments_delete",
        tags=["system-management.departments.id"],
        responses={
            200: DeleteDepartmentSerializer()
        }
    )
    def delete(request, department_id=None):
        logger.info(f"authenticated: {request.user}")
        department = get_department_by_id(department_id)
        if department is None:
            raise Http404
        # Copy department so that we can return this data from our delete response
        response = {
            'operation': 'delete',
            'domain': 'system',
            'model': 'Department',
            'data': department
        }
        response_serializer = DeleteDepartmentSerializer(response)
        response_serializer_data = response_serializer.data

        delete_department(department)

        return Response(response_serializer_data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="departments_update",
        tags=["system-management.departments.id"],
        request_body=UpdateDepartmentSerializer,
        responses={
            200: ReadDepartmentSerializer()
        }
    )
    def put(request, department_id=None):
        logger.info(f"authenticated: {request.user}")

        department = get_department_by_id(department_id)

        if department is None:
            raise Http404

        department_serializer = UpdateDepartmentSerializer(
            data=request.data
        )

        department_serializer.is_valid(raise_exception=True)

        update_department(
            department,
            department_serializer.validated_data.get('department_name', department.department_name)
        )
        # NOTE: Re-serialize to fetch more detailed data
        department_serializer = ReadDepartmentSerializer(
            department
        )
        return Response(department_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="departments_patch",
        tags=["system-management.departments.id"],
        request_body=UpdateDepartmentSerializer,
        responses={
            200: ReadDepartmentSerializer()
        }
    )
    def patch(request, department_id=None):
        logger.info(f"authenticated: {request.user}")

        department = get_department_by_id(department_id)
        if department is None:
            raise Http404

        department_serializer = UpdateDepartmentSerializer(
            data=request.data,
            partial=True
        )
        department_serializer.is_valid(raise_exception=True)

        update_department(
            department,
            department_serializer.validated_data.get('department_name', department.department_name)
        )
        # NOTE: Re-serialize to fetch more detailed data
        department_serializer = ReadDepartmentSerializer(department)
        return Response(department_serializer.data)
