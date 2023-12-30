from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Permissions
from domain.user.permissions.groups import IsAdminOrHumanResource

# Serializers
from .serializers import ReadGovernmentInformationSerializer, \
    CreateGovernmentInformationSerializer, PaginateReadGovernmentInformationSerializer, \
    PaginateQueryReadGovernmentInformationSerializer

# Services
from domain.user.services.government_information import get_government_informations, create_government_information

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class GovernmentInformationsAPIView(APIView):

    permission_classes = (IsAdminOrHumanResource,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadGovernmentInformationSerializer()
        },
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="government_informations_list",
        tags=["user-management.government-informations"],
        query_serializer=PaginateQueryReadGovernmentInformationSerializer()
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        government_informations = get_government_informations()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(government_informations, request)
        government_information_serializer = ReadGovernmentInformationSerializer(result_page, many=True)
        return paginator.get_paginated_response(government_information_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateGovernmentInformationSerializer,
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="government_informations_create",
        tags=["user-management.government-informations"],
        responses={
            200: ReadGovernmentInformationSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        government_information_serializer = CreateGovernmentInformationSerializer(data=request.data)
        government_information_serializer.is_valid(raise_exception=True)

        government_information = create_government_information(
            user=government_information_serializer.validated_data['user'], 
            sss_no=government_information_serializer.validated_data['sss_no'], 
            tin=government_information_serializer.validated_data['tin'], 
            philhealth=government_information_serializer.validated_data['philhealth'], 
            hdmf=government_information_serializer.validated_data['hdmf'], 
            prc_license_no=government_information_serializer.validated_data['prc_license_no'], 
            passport_no=government_information_serializer.validated_data['passport_no'], 
            tax_status=government_information_serializer.validated_data['tax_status'], 
            rdo_number=government_information_serializer.validated_data['rdo_number']
        )
        government_information_serializer = ReadGovernmentInformationSerializer(government_information)
        return Response(government_information_serializer.data)
