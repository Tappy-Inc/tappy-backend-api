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


def send_forgot_password_email(email: str, opt_code: int) -> bool:
    logger.info(f"Password reset request received for: {email}")
    send_email(
        from_email='support@tappy.com.ph',
        to=[email],
        subject='Password Reset Request',
        html=f'<p>You have requested a password reset. Please use the following token: {opt_code}</p>'
    )
    logger.info(f"Password reset email sent to: {email}")
    return True