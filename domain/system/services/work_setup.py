from typing import List

# Models
from domain.system.models import WorkSetup

import logging
logger = logging.getLogger(__name__)


def get_work_setups() -> List[WorkSetup]:
    work_setups = WorkSetup.objects.all().order_by('id')
    logger.info(f"{work_setups} fetched")
    return work_setups


def get_work_setup_by_id(work_setup_id: int) -> WorkSetup:
    work_setup = WorkSetup.objects.filter(id=work_setup_id).first()
    logger.info(f"{work_setup} fetched")
    return work_setup


def delete_work_setup(work_setup: WorkSetup) -> WorkSetup:
    work_setup.delete()
    logger.info(f"{work_setup} has been deleted.")
    return work_setup


def create_work_setup(work_setup: str) -> WorkSetup:
    work_setup = WorkSetup.objects.create(work_setup=work_setup)
    logger.info(f"\"{work_setup}\" has been created.")
    return work_setup


def update_work_setup(work_setup: WorkSetup, new_work_setup: str) -> WorkSetup:
    work_setup.work_setup = new_work_setup
    work_setup.save()

    logger.info(f"\"{work_setup}\" has been updated.")
    return work_setup
