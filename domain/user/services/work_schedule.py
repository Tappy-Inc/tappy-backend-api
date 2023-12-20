from django.utils import timezone
from typing import List
from django.contrib.auth.models import User
from domain.user.models import WorkSchedule

import logging
logger = logging.getLogger(__name__)

def get_work_schedules() -> List[WorkSchedule]:
    work_schedules = WorkSchedule.objects.all().order_by('id')
    logger.info(f"{work_schedules} fetched")
    return work_schedules

def get_work_schedule_by_user(user: User) -> List[WorkSchedule]:
    work_schedules = WorkSchedule.objects.filter(user=user).order_by('id')
    logger.info(f"Work schedules for user {user.username} fetched")
    return work_schedules

def get_work_schedule_by_id(work_schedule_id: int) -> WorkSchedule:
    work_schedule = WorkSchedule.objects.filter(id=work_schedule_id).first()
    logger.info(f"{work_schedule} fetched")
    return work_schedule

def delete_work_schedule(work_schedule: WorkSchedule) -> WorkSchedule:
    work_schedule.delete()
    logger.info(f"{work_schedule} has been deleted.")
    return work_schedule

def create_work_schedule(
        user: User, 
        day_of_week: str, 
        shift_start: str, 
        shift_end: str, 
        is_rest_day: bool
    ) -> WorkSchedule:
    work_schedule = WorkSchedule.objects.create(
        user=user, 
        day_of_week=day_of_week, 
        shift_start=shift_start, 
        shift_end=shift_end, 
        is_rest_day=is_rest_day
    )
    logger.info(f"\"{work_schedule}\" has been created.")
    return work_schedule

def update_work_schedule(
        work_schedule: WorkSchedule,
        new_day_of_week: str, 
        new_shift_start: str, 
        new_shift_end: str, 
        new_is_rest_day: bool
    ) -> WorkSchedule:
    work_schedule.day_of_week = new_day_of_week
    work_schedule.shift_start = new_shift_start
    work_schedule.shift_end = new_shift_end
    work_schedule.is_rest_day = new_is_rest_day
    work_schedule.updated_at = timezone.now()
    work_schedule.save()
    logger.info(f"\"{work_schedule}\" has been updated.")
    return work_schedule

