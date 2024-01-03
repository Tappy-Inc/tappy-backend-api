from django.utils import timezone
from typing import List

# Reset Password
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# Models
from domain.user.models.User import User

# Mailer
from domain.mailer.services.resend import send_email

import logging
logger = logging.getLogger(__name__)


def get_users() -> List[User]:
    users = User.objects.all().order_by('id')
    logger.info(f"{users} fetched")
    return users


def get_user_by_id(user_id: int) -> User:
    user = User.objects.filter(id=user_id).first()
    logger.info(f"{user} fetched")
    return user


def get_user_by_email(email: str) -> User:
    user = User.objects.filter(email=email).first()
    logger.info(f"{user} fetched by email")
    return user


def delete_user(user: User) -> User:
    user.delete()
    logger.info(f"{user} has been deleted.")
    return user


def create_user(username: str, password: str, first_name: str, last_name: str, email: str) -> User:
    user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
    logger.info(f"\"{user}\" has been created.")
    return user


def update_user(
        user: User,
        new_username: str,
        new_password: str,
        new_first_name: str,
        new_last_name: str,
        new_email: str
    ) -> User:
    user.username = new_username
    user.set_password(new_password)
    user.first_name = new_first_name
    user.last_name = new_last_name
    user.email = new_email
    user.updated_at = timezone.now()
    user.save()
    logger.info(f"\"{user}\" has been updated.")
    return user


def change_password(user: User, new_password: str) -> User:
    user.set_password(new_password)
    user.updated_at = timezone.now()
    user.save()
    logger.info(f"Password for \"{user}\" has been updated.")
    return user


# TODO: Refactor Mailer and use Mailer Template
def forgot_password(user: User) -> bool:
    logger.info(f"Attempting to reset password for email: {user.email}")
    # Generate a password reset token using Django's PasswordResetTokenGenerator
    token_generator = PasswordResetTokenGenerator()
    password_reset_token = token_generator.make_token(user)
    user.password_reset_token = password_reset_token
    user.save()
    logger.info(f"Password reset token generated for user: {user}")
    send_email(
        from_email='support@tappy.com.ph',
        to=[user.email],
        subject='Password Reset Request',
        html=f'<p>You have requested a password reset. Please use the following token: {password_reset_token}</p>'
    )
    logger.info(f"Password reset email sent to: {user.email}")
    return True


def reset_password(user: User, reset_code: str, new_password: str) -> bool:
    # Validate the reset code using Django's PasswordResetTokenGenerator
    token_generator = PasswordResetTokenGenerator()
    if not token_generator.check_token(user, reset_code):
        logger.error(f"Invalid reset code for email: {user.email}")
        return False
    user.set_password(new_password)
    user.password_reset_token = None
    user.updated_at = timezone.now()
    user.save()
    logger.info(f"Password for \"{user}\" has been updated.")
    return True
