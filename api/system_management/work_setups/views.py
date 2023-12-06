from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .serializers import ReadWorkSetupSerializer, \
    CreateWorkSetupSerializer, PaginateReadWorkSetupSerializer, \
    PaginateQueryReadWorkSetupSerializer

from domain.system.services.work_setup import get_work_setups, create_work_setup

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class WorkSetupsAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadWorkSetupSerializer()
        },
        operation_id="work_setup_list",
        tags=["system-management.work-setups"],
        query_serializer=PaginateQueryReadWorkSetupSerializer()
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        work_setups = get_work_setups()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(work_setups, request)
        work_setup_serializer = ReadWorkSetupSerializer(result_page, many=True)
        return paginator.get_paginated_response(work_setup_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateWorkSetupSerializer,
        operation_description="description",
        operation_id="work_setup_create",
        tags=["system-management.work-setups"],
        responses={
            200: ReadWorkSetupSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        work_setup_serializer = CreateWorkSetupSerializer(data=request.data)
        work_setup_serializer.is_valid(raise_exception=True)
        work_setup = create_work_setup(work_setup_serializer.validated_data['work_setup'])
        work_setup_serializer = ReadWorkSetupSerializer(work_setup)
        return Response(work_setup_serializer.data)
