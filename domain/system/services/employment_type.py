from django.utils import timezone
from typing import List

# Models
from domain.system.models import EmploymentType

import logging
logger = logging.getLogger(__name__)


def get_employment_types() -> List[EmploymentType]:
    employment_types = EmploymentType.objects.all().order_by('id')
    logger.info(f"{employment_types} fetched")
    return employment_types


def get_employment_type_by_id(employment_type_id: int) -> EmploymentType:
    employment_type = EmploymentType.objects.filter(id=employment_type_id).first()
    logger.info(f"{employment_type} fetched")
    return employment_type


def delete_employment_type(employment_type: EmploymentType) -> EmploymentType:
    employment_type.delete()
    logger.info(f"{employment_type} has been deleted.")
    return employment_type


def create_employment_type(employment_type: str) -> EmploymentType:
    employment_type = EmploymentType.objects.create(employment_type=employment_type)
    logger.info(f"\"{employment_type}\" has been created.")
    return employment_type


def update_employment_type(
        employment_type: EmploymentType,
        new_employment_type: str
    ) -> EmploymentType:
    employment_type.employment_type = new_employment_type
    employment_type.updated_at = timezone.now()
    employment_type.save()
    logger.info(f"\"{employment_type}\" has been updated.")
    return employment_type
