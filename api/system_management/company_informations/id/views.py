# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Permissions
from domain.user.permissions.groups import IsAdmin

# Serializers
from .serializers import ReadCompanyInformationSerializer, \
    UpdateCompanyInformationSerializer, DeleteCompanyInformationSerializer

# Services
from domain.system.services.company_information import get_company_information_by_id, delete_company_information, update_company_information

# Django Shortcuts
from django.shortcuts import get_object_or_404
from django.http import Http404

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class CompanyInformationsIdAPIView(APIView):

    permission_classes = (IsAdmin,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadCompanyInformationSerializer()
        },
        operation_description="description",
        operation_id="company_informations_read",
        tags=["system-management.company_informations.id"],
    )
    def get(request, company_information_id=None):
        logger.info(f"authenticated: {request.user}")
        company_information = get_company_information_by_id(company_information_id)
        if company_information is None:
            raise Http404
        company_information_serializer = ReadCompanyInformationSerializer(company_information)
        return Response(company_information_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="company_informations_delete",
        tags=["system-management.company_informations.id"],
        responses={
            200: DeleteCompanyInformationSerializer()
        }
    )
    def delete(request, company_information_id=None):
        logger.info(f"authenticated: {request.user}")
        company_information = get_company_information_by_id(company_information_id)
        if company_information is None:
            raise Http404
        # Copy company_information so that we can return this data from our delete response
        response = {
            'operation': 'delete',
            'domain': 'system',
            'model': 'CompanyInformation',
            'data': company_information
        }
        response_serializer = DeleteCompanyInformationSerializer(response)
        response_serializer_data = response_serializer.data

        delete_company_information(company_information)

        return Response(response_serializer_data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="company_informations_update",
        tags=["system-management.company_informations.id"],
        request_body=UpdateCompanyInformationSerializer,
        responses={
            200: ReadCompanyInformationSerializer()
        }
    )
    def put(request, company_information_id=None):
        logger.info(f"authenticated: {request.user}")

        company_information = get_company_information_by_id(company_information_id)

        if company_information is None:
            raise Http404

        company_information_serializer = UpdateCompanyInformationSerializer(
            data=request.data
        )

        company_information_serializer.is_valid(raise_exception=True)

        update_company_information(
            company_information,
            company_information_serializer.validated_data.get('company_name', company_information.company_name),
            company_information_serializer.validated_data.get('address', company_information.address),
            company_information_serializer.validated_data.get('number', company_information.number),
            company_information_serializer.validated_data.get('company_size', company_information.company_size),
            company_information_serializer.validated_data.get('industry', company_information.industry)
        )
        # NOTE: Re-serialize to fetch more detailed data
        company_information_serializer = ReadCompanyInformationSerializer(
            company_information
        )
        return Response(company_information_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="company_informations_patch",
        tags=["system-management.company_informations.id"],
        request_body=UpdateCompanyInformationSerializer,
        responses={
            200: ReadCompanyInformationSerializer()
        }
    )
    def patch(request, company_information_id=None):
        logger.info(f"authenticated: {request.user}")

        company_information = get_company_information_by_id(company_information_id)
        if company_information is None:
            raise Http404

        company_information_serializer = UpdateCompanyInformationSerializer(
            data=request.data,
            partial=True
        )
        company_information_serializer.is_valid(raise_exception=True)

        update_company_information(
            company_information,
            company_information_serializer.validated_data.get('company_name', company_information.company_name),
            company_information_serializer.validated_data.get('address', company_information.address),
            company_information_serializer.validated_data.get('number', company_information.number),
            company_information_serializer.validated_data.get('company_size', company_information.company_size),
            company_information_serializer.validated_data.get('industry', company_information.industry)
        )
        # NOTE: Re-serialize to fetch more detailed data
        company_information_serializer = ReadCompanyInformationSerializer(company_information)
        return Response(company_information_serializer.data)
