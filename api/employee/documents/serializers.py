from rest_framework import serializers

# Models
from domain.user.models import Document

import logging
logger = logging.getLogger(__name__)


class ReadDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "employee.documents.ReadDocumentSerializer"
        model = Document
        fields = [
            'id',
            'user',
            'file_name',
            'file_type',
            'file_source',
            'file_upload',
            'file_size'
        ]


class CreateDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "employee.documents.CreateDocumentSerializer"
        model = Document
        fields = [
            'file_upload'
        ]
