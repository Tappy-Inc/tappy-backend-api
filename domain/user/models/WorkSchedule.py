from django.db import models
from domain.common.models.Base import BaseModel
from django.contrib.auth.models import User

import logging
logger = logging.getLogger(__name__)

class WorkSchedule(BaseModel):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='work_schedules', on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    is_rest_day = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.day_of_week}'
