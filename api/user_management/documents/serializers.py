from rest_framework import serializers

# Models
from domain.user.models import Document

import logging
logger = logging.getLogger(__name__)


class ReadDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user-management.documents.ReadDocumentSerializer"
        model = Document
        fields = [
            'id',
            'user',
            'file_name',
            'file_type',
            'file_source',
            'file_upload'
        ]


class CreateDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "user-management.documents.CreateDocumentSerializer"
        model = Document
        fields = [
            'user',
            'file_upload'
        ]


class PaginateReadDocumentSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.documents.PaginateReadDocumentSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadDocumentSerializer(many=True)


class PaginateQueryReadDocumentSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.documents.PaginateQueryReadDocumentSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
