from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Permissions
from domain.user.permissions.groups import IsAdmin

# Serializers
from .serializers import ReadEmploymentTypeSerializer, \
    CreateEmploymentTypeSerializer, PaginateReadEmploymentTypeSerializer, \
    PaginateQueryReadEmploymentTypeSerializer

# Services
from domain.system.services.employment_type import get_employment_types, create_employment_type

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class EmploymentTypesAPIView(APIView):

    permission_classes = (IsAdmin,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadEmploymentTypeSerializer()
        },
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="employment_type_list",
        tags=["system-management.employment-types"],
        query_serializer=PaginateQueryReadEmploymentTypeSerializer()
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        employment_types = get_employment_types()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(employment_types, request)
        employment_type_serializer = ReadEmploymentTypeSerializer(result_page, many=True)
        return paginator.get_paginated_response(employment_type_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateEmploymentTypeSerializer,
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="employment_type_create",
        tags=["system-management.employment-types"],
        responses={
            200: ReadEmploymentTypeSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        employment_type_serializer = CreateEmploymentTypeSerializer(data=request.data)
        employment_type_serializer.is_valid(raise_exception=True)
        employment_type = create_employment_type(employment_type_serializer.validated_data['employment_type'])
        employment_type_serializer = ReadEmploymentTypeSerializer(employment_type)
        return Response(employment_type_serializer.data)
