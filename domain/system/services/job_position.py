from typing import List

# Models
from domain.system.models import Department
from domain.system.models import JobPosition

import logging
logger = logging.getLogger(__name__)


def get_job_positions() -> List[JobPosition]:
    job_positions = JobPosition.objects.all().order_by('id')
    logger.info(f"{job_positions} fetched")
    return job_positions


def get_job_position_by_id(job_position_id: int) -> JobPosition:
    job_position = JobPosition.objects.filter(id=job_position_id).first()
    logger.info(f"{job_position} fetched")
    return job_position


def delete_job_position(job_position: JobPosition) -> JobPosition:
    job_position.delete()
    logger.info(f"{job_position} has been deleted.")
    return job_position


def get_job_positions_by_department(department: Department) -> List[JobPosition]:
    job_positions = JobPosition.objects.filter(department=department).order_by('id')
    logger.info(f"{job_positions} fetched from department {department}")
    return job_positions


def create_job_position(position_name: str, department: Department) -> JobPosition:
    job_position = JobPosition.objects.create(position_name=position_name, department=department)
    logger.info(f"\"{job_position}\" has been created.")
    return job_position


def update_job_position(
        job_position: JobPosition,
        new_position_name: str,
        department: Department
    ) -> JobPosition:
    job_position.position_name = new_position_name
    job_position.department = department
    job_position.save()
    logger.info(f"\"{job_position}\" has been updated.")
    return job_position
