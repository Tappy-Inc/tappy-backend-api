from django.db import models
from domain.common.models.Base import BaseModel
import logging

logger = logging.getLogger(__name__)


class WorkSetup(BaseModel):
    id = models.AutoField(primary_key=True)
    work_setup = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.work_setup
