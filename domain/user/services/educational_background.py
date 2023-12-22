from django.utils import timezone
from typing import List
from domain.user.models.User import User
from domain.user.models import EducationalBackground

import logging
logger = logging.getLogger(__name__)

def get_educational_backgrounds() -> List[EducationalBackground]:
    educational_backgrounds = EducationalBackground.objects.all().order_by('id')
    logger.info(f"{educational_backgrounds} fetched")
    return educational_backgrounds

def get_educational_background_by_id(educational_background_id: int) -> EducationalBackground:
    educational_background = EducationalBackground.objects.filter(id=educational_background_id).first()
    logger.info(f"{educational_background} fetched")
    return educational_background

def delete_educational_background(educational_background: EducationalBackground) -> EducationalBackground:
    educational_background.delete()
    logger.info(f"{educational_background} has been deleted.")
    return educational_background

def create_educational_background(
        user: User, 
        education_type: str, 
        school: str, 
        from_year: str, 
        to_year: str, 
        degree: str
    ) -> EducationalBackground:
    educational_background = EducationalBackground.objects.create(
        user=user, 
        education_type=education_type, 
        school=school, 
        from_year=from_year, 
        to_year=to_year, 
        degree=degree
    )
    logger.info(f"\"{educational_background}\" has been created.")
    return educational_background

def update_educational_background(
        educational_background: EducationalBackground,
        new_education_type: str, 
        new_school: str, 
        new_from_year: str, 
        new_to_year: str, 
        new_degree: str
    ) -> EducationalBackground:
    educational_background.education_type = new_education_type
    educational_background.school = new_school
    educational_background.from_year = new_from_year
    educational_background.to_year = new_to_year
    educational_background.degree = new_degree
    educational_background.updated_at = timezone.now()
    educational_background.save()
    logger.info(f"\"{educational_background}\" has been updated.")
    return educational_background
