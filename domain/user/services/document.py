from django.utils import timezone
from typing import List
from domain.user.models.User import User
from domain.user.models import Document

import logging
logger = logging.getLogger(__name__)

def get_documents() -> List[Document]:
    documents = Document.objects.all().order_by('id')
    logger.info(f"{documents} fetched")
    return documents

def get_document_by_id(document_id: int) -> Document:
    document = Document.objects.filter(id=document_id).first()
    logger.info(f"{document} fetched")
    return document

def delete_document(document: Document) -> Document:
    document.delete()
    logger.info(f"{document} has been deleted.")
    return document

def create_document(
        user: User, 
        file_name: str, 
        file_type: str, 
        file_size: int,
        file_source: str, 
        file_upload
    ) -> Document:
    document = Document.objects.create(
        user=user, 
        file_name=file_name, 
        file_type=file_type, 
        file_size=file_size,
        file_source=file_source, 
        file_upload=file_upload
    )
    logger.info(f"\"{document}\" has been created.")
    return document

def update_document(
        document: Document,
        new_file_name: str, 
        new_file_type: str, 
        new_file_size: int,
        new_file_source: str, 
        new_file_upload
    ) -> Document:
    document.file_name = new_file_name
    document.file_type = new_file_type
    document.file_size = new_file_size
    document.file_source = new_file_source
    document.file_upload = new_file_upload
    document.updated_at = timezone.now()
    document.save()
    logger.info(f"\"{document}\" has been updated.")
    return document
