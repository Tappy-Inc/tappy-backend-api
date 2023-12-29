from typing import List

# Models
from domain.mailer.models.Template import Template

import logging
logger = logging.getLogger(__name__)


def get_templates() -> List[Template]:
    templates = Template.objects.all().order_by('id')
    logger.info(f"{templates} fetched")
    return templates


def get_template_by_id(template_id: int) -> Template:
    template = Template.objects.filter(id=template_id).first()
    logger.info(f"{template} fetched")
    return template


def get_template_by_name(template_name: str) -> Template:
    template = Template.objects.filter(name=template_name).first()
    logger.info(f"{template} fetched")
    return template


def delete_template(template: Template) -> Template:
    template.delete()
    logger.info(f"{template} has been deleted.")
    return template


def create_template(
        name: str, 
        subject: str, 
        body: str
    ) -> Template:
    template = Template.objects.create(
        name=name, 
        subject=subject, 
        body=body
    )
    logger.info(f"\"{template}\" has been created.")
    return template


def update_template(
        template: Template,
        new_name: str, 
        new_subject: str, 
        new_body: str
    ) -> Template:
    template.name = new_name
    template.subject = new_subject
    template.body = new_body
    template.save()
    logger.info(f"\"{template}\" has been updated.")
    return template
