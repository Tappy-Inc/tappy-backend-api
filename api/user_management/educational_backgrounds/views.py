from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Permissions
from domain.user.permissions.groups import IsAdminOrHumanResource

# Serializers
from .serializers import ReadEducationalBackgroundSerializer, \
    CreateEducationalBackgroundSerializer, PaginateReadEducationalBackgroundSerializer, \
    PaginateQueryReadEducationalBackgroundSerializer

from domain.user.services.educational_background import get_educational_backgrounds, create_educational_background

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class EducationalBackgroundsAPIView(APIView):

    permission_classes = (IsAdminOrHumanResource,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadEducationalBackgroundSerializer()
        },
        operation_id="educational_backgrounds_list",
        tags=["user-management.educational-backgrounds"],
        query_serializer=PaginateQueryReadEducationalBackgroundSerializer()
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        educational_backgrounds = get_educational_backgrounds()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(educational_backgrounds, request)
        educational_background_serializer = ReadEducationalBackgroundSerializer(result_page, many=True)
        return paginator.get_paginated_response(educational_background_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateEducationalBackgroundSerializer,
        operation_description="description",
        operation_id="educational_backgrounds_create",
        tags=["user-management.educational-backgrounds"],
        responses={
            200: ReadEducationalBackgroundSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        educational_background_serializer = CreateEducationalBackgroundSerializer(data=request.data)
        educational_background_serializer.is_valid(raise_exception=True)

        educational_background = create_educational_background(
            user=educational_background_serializer.validated_data['user'], 
            education_type=educational_background_serializer.validated_data['education_type'], 
            school=educational_background_serializer.validated_data['school'], 
            from_year=educational_background_serializer.validated_data['from_year'], 
            to_year=educational_background_serializer.validated_data['to_year'], 
            degree=educational_background_serializer.validated_data['degree']
        )
        educational_background_serializer = ReadEducationalBackgroundSerializer(educational_background)
        return Response(educational_background_serializer.data)


