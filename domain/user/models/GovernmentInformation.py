from django.db import models
from simple_history.models import HistoricalRecords
from domain.common.models.Base import BaseModel
from django.contrib.auth.models import User

import logging

logger = logging.getLogger(__name__)


class GovernmentInformation(BaseModel):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    sss_no = models.CharField(max_length=30, null=True, blank=True)
    tin = models.CharField(max_length=30, null=True, blank=True)
    philhealth = models.CharField(max_length=30, null=True, blank=True)
    hdmf = models.CharField(max_length=30, null=True, blank=True)
    prc_license_no = models.CharField(max_length=30, null=True, blank=True)
    passport_no = models.CharField(max_length=30, null=True, blank=True)
    tax_status = models.CharField(max_length=30, null=True, blank=True)
    rdo_number = models.CharField(max_length=30, null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.user.username
