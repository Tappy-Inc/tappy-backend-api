from django.db import models
from domain.common.models.Base import BaseModel
from domain.user.models.User import User
from domain.system.models.Gender import Gender
# Library: django_countries
from django_countries.fields import CountryField


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
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField()
    civil_status = models.CharField(max_length=10, choices=CIVIL_STATUS_CHOICES, blank=True)
    employee_id = models.CharField(max_length=30, unique=True)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    manager = models.ForeignKey(User, related_name='managed_profile', on_delete=models.SET_NULL, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    nationality = CountryField(blank=True, null=True)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)

    def __str__(self):  # pragma: no cover
        return self.user.username



