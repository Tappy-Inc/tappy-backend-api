from django.utils import timezone
from typing import List

# Models
from domain.system.models import CompanyInformation

import logging
logger = logging.getLogger(__name__)


def get_company_informations() -> List[CompanyInformation]:
    company_informations = CompanyInformation.objects.all().order_by('id')
    logger.info(f"{company_informations} fetched")
    return company_informations


def get_company_information_by_id(company_information_id: int) -> CompanyInformation:
    company_information = CompanyInformation.objects.filter(id=company_information_id).first()
    logger.info(f"{company_information} fetched")
    return company_information


def delete_company_information(company_information: CompanyInformation) -> CompanyInformation:
    company_information.delete()
    logger.info(f"{company_information} has been deleted.")
    return company_information


def create_company_information(company_name: str, address: str, number: str, company_size: int, industry: str) -> CompanyInformation:
    company_information = CompanyInformation.objects.create(company_name=company_name, address=address, number=number, company_size=company_size, industry=industry)
    logger.info(f"\"{company_information}\" has been created.")
    return company_information


def update_company_information(
        company_information: CompanyInformation,
        new_company_name: str,
        new_address: str,
        new_number: str,
        new_company_size: int,
        new_industry: str
    ) -> CompanyInformation:
    company_information.company_name = new_company_name
    company_information.address = new_address
    company_information.number = new_number
    company_information.company_size = new_company_size
    company_information.industry = new_industry
    company_information.updated_at = timezone.now()
    company_information.save()
    logger.info(f"\"{company_information}\" has been updated.")
    return company_information
