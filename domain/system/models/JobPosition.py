from django.db import models
from simple_history.models import HistoricalRecords
from domain.common.models.Base import BaseModel
from domain.system.models.Department import Department
import logging

logger = logging.getLogger(__name__)


class JobPosition(BaseModel):
    id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='job_positions')
    history = HistoricalRecords()

    def __str__(self):
        return self.position_name
