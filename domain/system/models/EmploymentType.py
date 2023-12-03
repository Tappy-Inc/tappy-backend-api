from django.db import models
from simple_history.models import HistoricalRecords
from domain.common.models.Base import BaseModel

import logging

logger = logging.getLogger(__name__)


class EmploymentType(BaseModel):
    id = models.AutoField(primary_key=True)
    employment_type = models.CharField(max_length=50, unique=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.employment_type
