# Django
from asgiref.sync import sync_to_async

# Services
from domain.user.services.user import get_user_by_id
from domain.mailer.services.mailer import get_template_by_name
from domain.mailer.services.resend import send_email

import logging
logger = logging.getLogger(__name__)


def send_welcome_email(msg_data: dict):
    user_id = msg_data['data']['user_id']

    user = get_user_by_id(user_id)
    if user is None:
        logger.error(f"User {user} does not exist.")
        return
    
    template = get_template_by_name('welcome_email')
    if template is None:
        logger.error(f"Template {template} does not exist.")
        return
    
    response = send_email(
        to=[user.email],
        subject=template.subject,
        html=template.body,
    )
    logger.info(response)
    return response