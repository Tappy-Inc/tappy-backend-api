from django.db import models
from domain.common.models.Base import BaseModel
import logging

logger = logging.getLogger(__name__)


class Department(BaseModel):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.department_name
