from django.db import models
from domain.common.models.Base import BaseModel

# Models
from domain.mailer.models.FromEmail import FromEmail

import logging
logger = logging.getLogger(__name__)


class Template(BaseModel):

    id = models.AutoField(primary_key=True)
    from_email = models.ForeignKey(FromEmail, related_name='templates', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):  # pragma: no cover
        return self.name

