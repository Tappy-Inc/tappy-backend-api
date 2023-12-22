# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Permissions
from domain.user.permissions.groups import IsAdmin

# Serializers
from .serializers import ReadDepartmentSerializer, \
    CreateDepartmentSerializer, PaginateReadDepartmentSerializer, \
    PaginateQueryReadDepartmentSerializer

# Services
from domain.system.services.department import get_departments, create_department

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class DepartmentsAPIView(APIView):

    permission_classes = (IsAdmin,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadDepartmentSerializer()
        },
        operation_id="departments_list",
        tags=["system-management.departments"],
        query_serializer=PaginateQueryReadDepartmentSerializer()
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        departments = get_departments()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(departments, request)
        department_serializer = ReadDepartmentSerializer(result_page, many=True)
        return paginator.get_paginated_response(department_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateDepartmentSerializer,
        operation_description="description",
        operation_id="departments_create",
        tags=["system-management.departments"],
        responses={
            200: ReadDepartmentSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        department_serializer = CreateDepartmentSerializer(data=request.data)
        department_serializer.is_valid(raise_exception=True)
        department = create_department(department_serializer.validated_data['department_name'])
        department_serializer = ReadDepartmentSerializer(department)
        return Response(department_serializer.data)
