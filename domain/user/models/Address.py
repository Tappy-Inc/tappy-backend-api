from django.db import models
from domain.common.models.Base import BaseModel
from domain.user.models.User import User

import logging
logger = logging.getLogger(__name__)


class Address(BaseModel):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    baranggay = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=255)

    def __str__(self):  # pragma: no cover
        return f'{self.address}, {self.city}, {self.state}, {self.postal_code}, {self.country}'