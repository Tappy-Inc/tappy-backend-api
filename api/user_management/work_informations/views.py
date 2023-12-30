from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Permissions
from domain.user.permissions.groups import IsAdminOrHumanResource

# Serializers
from .serializers import ReadWorkInformationSerializer, \
    CreateWorkInformationSerializer, PaginateReadWorkInformationSerializer, \
    PaginateQueryReadWorkInformationSerializer

# Services
from domain.user.services.work_information import get_work_informations, create_work_information

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class WorkInformationsAPIView(APIView):

    permission_classes = (IsAdminOrHumanResource,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadWorkInformationSerializer()
        },
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="work_informations_list",
        tags=["user-management.work-informations"],
        query_serializer=PaginateQueryReadWorkInformationSerializer()
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        work_informations = get_work_informations()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(work_informations, request)
        work_information_serializer = ReadWorkInformationSerializer(result_page, many=True)
        return paginator.get_paginated_response(work_information_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateWorkInformationSerializer,
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="work_informations_create",
        tags=["user-management.work-informations"],
        responses={
            200: ReadWorkInformationSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        work_information_serializer = CreateWorkInformationSerializer(data=request.data)
        work_information_serializer.is_valid(raise_exception=True)

        work_information = create_work_information(
            user=work_information_serializer.validated_data['user'], 
            department=work_information_serializer.validated_data['department'], 
            job_level=work_information_serializer.validated_data['job_level'], 
            employment_type=work_information_serializer.validated_data['employment_type'], 
            work_setup=work_information_serializer.validated_data['work_setup']
        )
        work_information_serializer = ReadWorkInformationSerializer(work_information)
        return Response(work_information_serializer.data)
