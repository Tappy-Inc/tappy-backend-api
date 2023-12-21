from django.db import models
from simple_history.models import HistoricalRecords
from domain.common.models.Base import BaseModel
from django.contrib.auth.models import User

import logging
logger = logging.getLogger(__name__)


class Document(BaseModel):
    
    user = models.ForeignKey(User, related_name='documents', on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255, null=False, blank=False)
    file_type = models.CharField(max_length=255, null=False, blank=False)
    file_source = models.CharField(max_length=255, null=False, blank=False)
    file_upload = models.FileField(upload_to='documents/', null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.file_name
