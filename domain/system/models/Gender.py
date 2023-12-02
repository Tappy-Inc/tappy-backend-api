from django.db import models
from domain.common.models.Base import BaseModel
import logging

logger = logging.getLogger(__name__)


class Gender(BaseModel):
    id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.gender
