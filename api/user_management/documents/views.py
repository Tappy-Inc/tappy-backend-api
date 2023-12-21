from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .serializers import ReadDocumentSerializer, \
    CreateDocumentSerializer, PaginateReadDocumentSerializer, \
    PaginateQueryReadDocumentSerializer

from domain.user.services.document import get_documents, create_document

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class DocumentsAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: PaginateReadDocumentSerializer()
        },
        operation_id="documents_list",
        tags=["user-management.documents"],
        query_serializer=PaginateQueryReadDocumentSerializer()
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        documents = get_documents()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(documents, request)
        document_serializer = ReadDocumentSerializer(result_page, many=True)
        return paginator.get_paginated_response(document_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateDocumentSerializer,
        operation_description="description",
        operation_id="documents_create",
        tags=["user-management.documents"],
        responses={
            200: ReadDocumentSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        document_serializer = CreateDocumentSerializer(data=request.data)
        document_serializer.is_valid(raise_exception=True)

        document = create_document(
            user=document_serializer.validated_data['user'], 
            file_name=document_serializer.validated_data['file_name'], 
            file_type=document_serializer.validated_data['file_type'], 
            file_source=document_serializer.validated_data['file_source'], 
            file_upload=document_serializer.validated_data['file_upload']
        )
        document_serializer = ReadDocumentSerializer(document)
        return Response(document_serializer.data)

