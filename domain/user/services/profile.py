from datetime import date
from django.utils import timezone
from typing import List
# Library: django_countries
from django_countries.fields import CountryField

# Models
from domain.user.models.User import User
from domain.system.models.Gender import Gender
from domain.user.models import Profile

import logging
logger = logging.getLogger(__name__)


def get_profiles() -> List[Profile]:
    profiles = Profile.objects.all().order_by('id')
    logger.info(f"{profiles} fetched")
    return profiles


def get_profile_by_id(profile_id: int) -> Profile:
    profile = Profile.objects.filter(id=profile_id).first()
    logger.info(f"{profile} fetched")
    return profile


def delete_profile(profile: Profile) -> Profile:
    profile.delete()
    logger.info(f"{profile} has been deleted.")
    return profile


def create_profile(
        user: User, 
        bio: str, 
        gender: Gender, 
        civil_status: str, 
        employee_id: str, 
        birth_date: date, 
        manager: User,
        mobile_number: str = None,
        nationality: CountryField = None
    ) -> Profile:
    profile = Profile.objects.create(
        user=user, 
        bio=bio, 
        gender=gender, 
        civil_status=civil_status, 
        employee_id=employee_id, 
        birth_date=birth_date, 
        manager=manager,
        mobile_number=mobile_number,
        nationality=nationality
    )
    logger.info(f"\"{profile}\" has been created.")
    return profile


def update_profile(
        profile: Profile,
        new_bio: str, 
        new_gender: Gender, 
        new_civil_status: str, 
        new_employee_id: str, 
        new_birth_date: date, 
        new_manager: User,
        new_mobile_number: str = None,
        new_nationality: CountryField = None
    ) -> Profile:
    profile.bio = new_bio
    profile.gender = new_gender
    profile.civil_status = new_civil_status
    profile.employee_id = new_employee_id
    profile.birth_date = new_birth_date
    profile.manager = new_manager
    profile.mobile_number = new_mobile_number
    profile.nationality = new_nationality
    profile.updated_at = timezone.now()
    profile.save()
    logger.info(f"\"{profile}\" has been updated.")
    return profile
