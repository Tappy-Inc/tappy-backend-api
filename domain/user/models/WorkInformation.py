from django.db import models
from domain.common.models.Base import BaseModel
from django.contrib.auth.models import User
from domain.system.models.Department import Department
from domain.system.models.JobLevel import JobLevel
from domain.system.models.EmploymentType import EmploymentType
from domain.system.models.WorkSetup import WorkSetup

import logging
logger = logging.getLogger(__name__)


class WorkInformation(BaseModel):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, related_name='work_information', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='work_information', on_delete=models.CASCADE)
    job_level = models.ForeignKey(JobLevel, related_name='work_information', on_delete=models.CASCADE)
    employment_type = models.ForeignKey(EmploymentType, related_name='work_information', on_delete=models.CASCADE)
    work_setup = models.ForeignKey(WorkSetup, related_name='work_information', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.department.department_name} - {self.job_level.level}'
