from django.db import models
from simple_history.models import HistoricalRecords
from domain.common.models.Base import BaseModel
from domain.user.models.User import User

import logging
logger = logging.getLogger(__name__)


class EducationalBackground(BaseModel):

    EDUCATION_TYPE_CHOICES = [
        ('College', 'College'),
        ('Highschool', 'Highschool'),
        ('Elementary', 'Elementary'),
        ('Vocational Course', 'Vocational Course'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    education_type = models.CharField(max_length=255, choices=EDUCATION_TYPE_CHOICES, null=False, blank=False)
    school = models.CharField(max_length=255, null=False, blank=False)
    from_year = models.DateField()
    to_year = models.DateField()
    degree = models.CharField(max_length=255, null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.user.username
