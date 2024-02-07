from django.db import models
from domain.common.models.Base import BaseModel
from domain.user.models.User import User

import logging
logger = logging.getLogger(__name__)


class Document(BaseModel):
    
    def user_directory_path(self, filename):
        return f"user_{self.user.id}/documents/{filename}"

    user = models.ForeignKey(User, related_name='documents', on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=255)
    file_source = models.CharField(max_length=255)
    file_upload = models.FileField(upload_to=user_directory_path)
    file_size = models.IntegerField()

    def __str__(self):
        return self.file_name
