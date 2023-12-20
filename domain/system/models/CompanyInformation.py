from django.db import models
from simple_history.models import HistoricalRecords
from domain.common.models.Base import BaseModel

import logging

logger = logging.getLogger(__name__)


class CompanyInformation(BaseModel):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    company_size = models.IntegerField()
    industry = models.CharField(max_length=50)
    history = HistoricalRecords()

    def __str__(self):
        return self.company_name
