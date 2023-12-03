from django.db import models
from domain.common.models.Base import BaseModel
# Library: django-simple-history
from simple_history.models import HistoricalRecords

import logging

logger = logging.getLogger(__name__)


class Gender(BaseModel):
    id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=10, unique=True)
    # Library: django-simple-history
    history = HistoricalRecords()

    def __str__(self):
        return self.gender
