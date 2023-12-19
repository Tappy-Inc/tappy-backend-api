from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ReadGovernmentInformationSerializer, UpdateGovernmentInformationSerializer, DeleteGovernmentInformationSerializer
from domain.user.services.government_information import get_government_information_by_id, delete_government_information, update_government_information

from django.shortcuts import get_object_or_404
from django.http import Http404

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class GovernmentInformationIdAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadGovernmentInformationSerializer()
        },
        operation_description="description",
        operation_id="government_informations_read",
        tags=["user-management.government-informations.id"],
    )
    def get(request, government_information_id=None):
        logger.info(f"authenticated: {request.user}")
        government_information = get_government_information_by_id(government_information_id)
        if government_information is None:
            raise Http404
        government_information_serializer = ReadGovernmentInformationSerializer(government_information)
        return Response(government_information_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="government_informations_delete",
        tags=["user-management.government-informations.id"],
        responses={
            200: DeleteGovernmentInformationSerializer()
        }
    )
    def delete(request, government_information_id=None):
        logger.info(f"authenticated: {request.user}")
        government_information = get_government_information_by_id(government_information_id)
        if government_information is None:
            raise Http404
        response = {
            'operation': 'delete',
            'domain': 'user_management',
            'model': 'GovernmentInformation',
            'data': government_information
        }
        response_serializer = DeleteGovernmentInformationSerializer(response)
        response_serializer_data = response_serializer.data

        delete_government_information(government_information)

        return Response(response_serializer_data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="government_informations_update",
        tags=["user-management.government-informations.id"],
        request_body=UpdateGovernmentInformationSerializer,
        responses={
            200: ReadGovernmentInformationSerializer()
        }
    )
    def put(request, government_information_id=None):
        logger.info(f"authenticated: {request.user}")

        government_information = get_government_information_by_id(government_information_id)

        if government_information is None:
            raise Http404

        government_information_serializer = UpdateGovernmentInformationSerializer(
            data=request.data
        )

        government_information_serializer.is_valid(raise_exception=True)

        update_government_information(
            government_information,
            government_information_serializer.validated_data.get('sss_no', government_information.sss_no),
            government_information_serializer.validated_data.get('tin', government_information.tin),
            government_information_serializer.validated_data.get('philhealth', government_information.philhealth),
            government_information_serializer.validated_data.get('hdmf', government_information.hdmf),
            government_information_serializer.validated_data.get('prc_license_no', government_information.prc_license_no),
            government_information_serializer.validated_data.get('passport_no', government_information.passport_no),
            government_information_serializer.validated_data.get('tax_status', government_information.tax_status),
            government_information_serializer.validated_data.get('rdo_number', government_information.rdo_number)
        )
        government_information_serializer = ReadGovernmentInformationSerializer(government_information)
        return Response(government_information_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="government_informations_patch",
        tags=["user-management.government-informations.id"],
        request_body=UpdateGovernmentInformationSerializer,
        responses={
            200: ReadGovernmentInformationSerializer()
        }
    )
    def patch(request, government_information_id=None):
        logger.info(f"authenticated: {request.user}")

        government_information = get_government_information_by_id(government_information_id)
        if government_information is None:
            raise Http404

        government_information_serializer = UpdateGovernmentInformationSerializer(
            data=request.data,
            partial=True
        )
        government_information_serializer.is_valid(raise_exception=True)

        update_government_information(
            government_information,
            government_information_serializer.validated_data.get('sss_no', government_information.sss_no),
            government_information_serializer.validated_data.get('tin', government_information.tin),
            government_information_serializer.validated_data.get('philhealth', government_information.philhealth),
            government_information_serializer.validated_data.get('hdmf', government_information.hdmf),
            government_information_serializer.validated_data.get('prc_license_no', government_information.prc_license_no),
            government_information_serializer.validated_data.get('passport_no', government_information.passport_no),
            government_information_serializer.validated_data.get('tax_status', government_information.tax_status),
            government_information_serializer.validated_data.get('rdo_number', government_information.rdo_number)
        )
        government_information_serializer = ReadGovernmentInformationSerializer(government_information)
        return Response(government_information_serializer.data)
