from django.utils import timezone
from typing import List

# Models
from domain.system.models import Department

import logging
logger = logging.getLogger(__name__)


def get_departments() -> List[Department]:
    departments = Department.objects.all().order_by('id')
    logger.info(f"{departments} fetched")
    return departments


def get_department_by_id(department_id: int) -> Department:
    department = Department.objects.filter(id=department_id).first()
    logger.info(f"{department} fetched")
    return department


def delete_department(department: Department) -> Department:
    department.delete()
    logger.info(f"{department} has been deleted.")
    return department


def create_department(department_name: str) -> Department:
    department = Department.objects.create(department_name=department_name)
    logger.info(f"\"{department}\" has been created.")
    return department


def update_department(
        department: Department,
        new_department_name: str
    ) -> Department:
    department.department_name = new_department_name
    department.updated_at = timezone.now()
    department.save()
    logger.info(f"\"{department}\" has been updated.")
    return department
