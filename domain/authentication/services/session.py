from typing import List
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

# Models
from django.contrib.auth.models import User
from domain.authentication.models import Session

import logging
logger = logging.getLogger(__name__)


def get_sessions() -> List[Session]:
    sessions = Session.objects.all().order_by('id')
    logger.info(f"{sessions} fetched")
    return sessions


def get_session_by_id(session_id: int) -> Session:
    session = Session.objects.filter(id=session_id).first()
    logger.info(f"{session} fetched")
    return session


def delete_session(session: Session) -> Session:
    session.delete()
    logger.info(f"{session} has been deleted.")
    return session


def create_session(user: User, session_key: str, session_data: str, expire_date: datetime) -> Session:
    session = Session.objects.create(user=user, session_key=session_key, session_data=session_data, expire_date=expire_date)
    logger.info(f"\"{session}\" has been created.")
    return session


def create_session_if_not_exists(user: User, session_key: str, session_data: str, expire_date: datetime) -> Session:
    try:
        session = Session.objects.get(session_key=session_key)
        logger.info(f"\"{session}\" already exists.")
    except ObjectDoesNotExist:
        session = Session.objects.create(user=user, session_key=session_key, session_data=session_data, expire_date=expire_date)
        logger.info(f"\"{session}\" has been created.")
    return session


def get_session_by_key_and_value(session_key: str, session_value: str) -> Session:
    session = Session.objects.filter(session_key=session_key, session_data=session_value).first()
    logger.info(f"{session} fetched by session_key and session_value")
    return session


def delete_sessions_by_key(session_key: str) -> None:
    sessions = Session.objects.filter(session_key=session_key)
    sessions.delete()
    logger.info(f"Sessions with key \"{session_key}\" have been deleted.")


def update_session(session: Session, new_session_key: str, new_session_data: str, new_expire_date: datetime) -> Session:
    session.session_key = new_session_key
    session.session_data = new_session_data
    session.expire_date = new_expire_date
    session.save()

    logger.info(f"\"{session}\" has been updated.")
    return session
