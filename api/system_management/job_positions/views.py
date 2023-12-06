from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .serializers import ReadJobPositionSerializer, \
    CreateJobPositionSerializer, PaginateReadJobPositionSerializer, \
    PaginateQueryReadJobPositionSerializer

from domain.system.services.job_position import get_job_positions, create_job_position

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class JobPositionsAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadJobPositionSerializer()
        },
        operation_id="job_positions_list",
        tags=["system-management.job_positions"],
        query_serializer=PaginateQueryReadJobPositionSerializer()
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        job_positions = get_job_positions()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(job_positions, request)
        job_position_serializer = ReadJobPositionSerializer(result_page, many=True)
        return paginator.get_paginated_response(job_position_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateJobPositionSerializer,
        operation_description="description",
        operation_id="job_positions_create",
        tags=["system-management.job_positions"],
        responses={
            200: ReadJobPositionSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        job_position_serializer = CreateJobPositionSerializer(data=request.data)
        job_position_serializer.is_valid(raise_exception=True)
        job_position = create_job_position(job_position_serializer.validated_data['position_name'], job_position_serializer.validated_data['department'])
        job_position_serializer = ReadJobPositionSerializer(job_position)
        return Response(job_position_serializer.data)
