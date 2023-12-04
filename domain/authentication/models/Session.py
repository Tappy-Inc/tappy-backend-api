from django.db import models
from django.contrib.auth.models import User

from domain.common.models.Base import BaseModel


class Session(BaseModel):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, unique=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    
    def __str__(self):
        return self.session_key
