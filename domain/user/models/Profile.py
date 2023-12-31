from django.db import models
from simple_history.models import HistoricalRecords
from domain.common.models.Base import BaseModel
from domain.user.models.User import User
from domain.system.models.Gender import Gender


import logging
logger = logging.getLogger(__name__)


class Profile(BaseModel):

    CIVIL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]
    
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    civil_status = models.CharField(max_length=10, choices=CIVIL_STATUS_CHOICES, blank=True)
    employee_id = models.CharField(max_length=30, unique=True)
    birth_date = models.DateField()
    manager = models.ForeignKey(User, related_name='managed_profile', on_delete=models.SET_NULL, null=True)
    history = HistoricalRecords()

    def __str__(self):  # pragma: no cover
        return self.user.username



