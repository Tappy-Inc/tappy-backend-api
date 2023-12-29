# Django
from asgiref.sync import sync_to_async

# Services
from domain.user.services.user import get_user_by_id
from domain.common.services.resend import send_email

import logging
logger = logging.getLogger(__name__)


def send_welcome_email(msg_data: dict):
    user_id = msg_data['data']['user_id']
    user = get_user_by_id(user_id)
    response = send_email(
        to=[user.email],
        subject="Welcome to Tappy Inc.!",
        html="""
        <html>
        <body>
        <h1>Welcome to Tappy Inc.!</h1>
        <p>We are thrilled to have you on board. At Tappy Inc., we believe in creating a collaborative and innovative environment where every member can contribute their unique skills and perspectives.</p>
        <p>We are confident that you will bring great value to our team and we look forward to the amazing things we will achieve together.</p>
        <p>Once again, welcome to the team!</p>
        <p>Best,</p>
        <p>The Tappy Inc. Team</p>
        </body>
        </html>
        """
    )
    logger.info(response)
    return response