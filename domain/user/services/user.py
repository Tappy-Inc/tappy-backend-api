from django.utils import timezone
from typing import List

# Models
from domain.user.models.User import User

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

