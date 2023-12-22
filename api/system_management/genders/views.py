# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Permissions
from domain.user.permissions.groups import IsAdmin

# Serializers
from .serializers import ReadGenderSerializer, \
    CreateGenderSerializer, PaginateReadGenderSerializer, \
    PaginateQueryReadGenderSerializer

# Services
from domain.system.services.gender import get_genders, create_gender

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import json
import logging
logger = logging.getLogger(__name__)


class GendersAPIView(APIView):

    permission_classes = (IsAdmin,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadGenderSerializer()
        },
        operation_id="genders_list",
        tags=["system-management.genders"],
        query_serializer=PaginateQueryReadGenderSerializer()
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        genders = get_genders()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(genders, request)
        gender_serializer = ReadGenderSerializer(result_page, many=True)
        return paginator.get_paginated_response(gender_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateGenderSerializer,
        operation_description="description",
        operation_id="genders_create",
        tags=["system-management.genders"],
        responses={
            200: ReadGenderSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        gender_serializer = CreateGenderSerializer(data=request.data)
        gender_serializer.is_valid(raise_exception=True)
        gender = create_gender(gender_serializer.validated_data['gender'])
        gender_serializer = ReadGenderSerializer(gender)
        return Response(gender_serializer.data)

