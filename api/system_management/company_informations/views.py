# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Permissions
from domain.user.permissions.groups import IsAdmin

# Serializers
from .serializers import ReadCompanyInformationSerializer, \
    CreateCompanyInformationSerializer, PaginateReadCompanyInformationSerializer, \
    PaginateQueryReadCompanyInformationSerializer

# Services
from domain.system.services.company_information import get_company_informations, create_company_information

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class CompanyInformationsAPIView(APIView):

    permission_classes = (IsAdmin,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadCompanyInformationSerializer()
        },
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="company_informations_list",
        tags=["system-management.company_informations"],
        query_serializer=PaginateQueryReadCompanyInformationSerializer()
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        company_informations = get_company_informations()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(company_informations, request)
        company_information_serializer = ReadCompanyInformationSerializer(result_page, many=True)
        return paginator.get_paginated_response(company_information_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateCompanyInformationSerializer,
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="company_informations_create",
        tags=["system-management.company_informations"],
        responses={
            200: ReadCompanyInformationSerializer()
        }
    )
    def post(request, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        company_information_serializer = CreateCompanyInformationSerializer(data=request.data)
        company_information_serializer.is_valid(raise_exception=True)
        company_information = create_company_information(
            company_information_serializer.validated_data['company_name'],
            company_information_serializer.validated_data['address'],
            company_information_serializer.validated_data['number'],
            company_information_serializer.validated_data['company_size'],
            company_information_serializer.validated_data['industry']
        )
        company_information_serializer = ReadCompanyInformationSerializer(company_information)
        return Response(company_information_serializer.data)
