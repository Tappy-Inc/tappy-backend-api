from django.utils import timezone
from typing import List
from domain.user.models.User import User
from domain.user.models import GovernmentInformation

import logging
logger = logging.getLogger(__name__)


def get_government_information_by_user(user: User) -> GovernmentInformation:
    government_information = GovernmentInformation.objects.filter(user=user).first()
    logger.info(f"{government_information} fetched for user {user.username}")
    return government_information

def get_government_informations() -> List[GovernmentInformation]:
    government_informations = GovernmentInformation.objects.all().order_by('id')
    logger.info(f"{government_informations} fetched")
    return government_informations

def get_government_information_by_id(government_information_id: int) -> GovernmentInformation:
    government_information = GovernmentInformation.objects.filter(id=government_information_id).first()
    logger.info(f"{government_information} fetched")
    return government_information

def delete_government_information(government_information: GovernmentInformation) -> GovernmentInformation:
    government_information.delete()
    logger.info(f"{government_information} has been deleted.")
    return government_information

def create_government_information(
        user: User, 
        sss_no: str, 
        tin: str, 
        philhealth: str, 
        hdmf: str, 
        prc_license_no: str, 
        passport_no: str, 
        tax_status: str, 
        rdo_number: str
    ) -> GovernmentInformation:
    government_information = GovernmentInformation.objects.create(
        user=user, 
        sss_no=sss_no, 
        tin=tin, 
        philhealth=philhealth, 
        hdmf=hdmf, 
        prc_license_no=prc_license_no, 
        passport_no=passport_no, 
        tax_status=tax_status, 
        rdo_number=rdo_number
    )
    logger.info(f"\"{government_information}\" has been created.")
    return government_information

def update_government_information(
        government_information: GovernmentInformation,
        new_sss_no: str, 
        new_tin: str, 
        new_philhealth: str, 
        new_hdmf: str, 
        new_prc_license_no: str, 
        new_passport_no: str, 
        new_tax_status: str, 
        new_rdo_number: str
    ) -> GovernmentInformation:
    government_information.sss_no = new_sss_no
    government_information.tin = new_tin
    government_information.philhealth = new_philhealth
    government_information.hdmf = new_hdmf
    government_information.prc_license_no = new_prc_license_no
    government_information.passport_no = new_passport_no
    government_information.tax_status = new_tax_status
    government_information.rdo_number = new_rdo_number
    government_information.updated_at = timezone.now()
    government_information.save()
    logger.info(f"\"{government_information}\" has been updated.")
    return government_information
