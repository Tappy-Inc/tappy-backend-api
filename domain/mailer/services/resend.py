import os
import resend
from typing import List

import logging
logger = logging.getLogger(__name__)


def send_email(from_email: str, to: List[str], subject: str, html: str) -> str:
    resend.api_key = os.environ.get('RESEND_API_KEY')
    params = {
        "from": from_email,
        "to": to,
        "subject": subject,
        "html": html,
    }
    email = resend.Emails.send(params)
    logger.info(f"Email {email} has been sent.")
    return email
