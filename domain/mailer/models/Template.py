from django.db import models
from simple_history.models import HistoricalRecords
from domain.common.models.Base import BaseModel

import logging
logger = logging.getLogger(__name__)


class Template(BaseModel):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    history = HistoricalRecords()

    def __str__(self):  # pragma: no cover
        return self.name

