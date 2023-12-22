from django.utils import timezone
from typing import List
from domain.user.models.User import User
from domain.system.models import Department, JobLevel, EmploymentType, WorkSetup
from domain.user.models import WorkInformation

import logging
logger = logging.getLogger(__name__)

def get_work_informations() -> List[WorkInformation]:
    work_informations = WorkInformation.objects.all().order_by('id')
    logger.info(f"{work_informations} fetched")
    return work_informations

def get_work_information_by_id(work_information_id: int) -> WorkInformation:
    work_information = WorkInformation.objects.filter(id=work_information_id).first()
    logger.info(f"{work_information} fetched")
    return work_information

def delete_work_information(work_information: WorkInformation) -> WorkInformation:
    work_information.delete()
    logger.info(f"{work_information} has been deleted.")
    return work_information

def create_work_information(
        user: User, 
        department: Department, 
        job_level: JobLevel, 
        employment_type: EmploymentType, 
        work_setup: WorkSetup
    ) -> WorkInformation:
    work_information = WorkInformation.objects.create(
        user=user, 
        department=department, 
        job_level=job_level, 
        employment_type=employment_type, 
        work_setup=work_setup
    )
    logger.info(f"\"{work_information}\" has been created.")
    return work_information

def update_work_information(
        work_information: WorkInformation,
        new_department: Department, 
        new_job_level: JobLevel, 
        new_employment_type: EmploymentType, 
        new_work_setup: WorkSetup
    ) -> WorkInformation:
    work_information.department = new_department
    work_information.job_level = new_job_level
    work_information.employment_type = new_employment_type
    work_information.work_setup = new_work_setup
    work_information.updated_at = timezone.now()
    work_information.save()
    logger.info(f"\"{work_information}\" has been updated.")
    return work_information
