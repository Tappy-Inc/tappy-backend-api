from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# NOTE: Enable file upload in Swagger Docs
from rest_framework.parsers import MultiPartParser 

# Permissions
from domain.user.permissions.groups import IsEmployee

# Serializers
from .serializers import ReadDocumentSerializer, CreateDocumentSerializer

# Services
from domain.user.services.document import get_documents_by_user, create_document


from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class DocumentAPIView(APIView):

    permission_classes = (IsEmployee,)

    # NOTE: Enable file upload in Swagger Docs
    parser_classes = (MultiPartParser,)
    
    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadDocumentSerializer(many=True)
        },
        operation_id="employee_documents_read",
        tags=["employee.documents"],
    )
    def get(request):
        documents = get_documents_by_user(user=request.user)
        serializer = ReadDocumentSerializer(documents, many=True)
        return Response(serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateDocumentSerializer,
        operation_description="description",
        operation_id="employee_documents_create",
        tags=["employee.documents"],
        responses={
            200: ReadDocumentSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        document_serializer = CreateDocumentSerializer(data=request.data)
        document_serializer.is_valid(raise_exception=True)

        file_upload = document_serializer.validated_data['file_upload']

        document = create_document(
            user=request.user,
            file_name=file_upload._name, 
            file_type=file_upload.content_type,
            file_size=file_upload.size,
            file_source='upload', 
            file_upload=file_upload
        )
        document_serializer = ReadDocumentSerializer(document)
        return Response(document_serializer.data)
