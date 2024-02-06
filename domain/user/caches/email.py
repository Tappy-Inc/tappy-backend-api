from django.core.cache import cache

import logging
logger = logging.getLogger(__name__)


def store_reset_password_otp_code(email: str, otp_code: str, expiry: int):
    """
    Cache the OTP code for password reset against the user's email.
    The OTP code will be expired after the specified expiry time.
    """
    cache_key = f"reset_password_otp_code_{email}"
    cache.set(cache_key, otp_code, expiry)
    logger.info(f"OTP code for email: {email} has been cached with expiry time: {expiry}")


def retrieve_reset_password_otp_code(email: str) -> int:
    """
    Retrieve the OTP code for password reset against the user's email.
    """
    cache_key = f"reset_password_otp_code_{email}"
    otp_code = cache.get(cache_key)
    if otp_code is None:
        logger.info(f"No OTP code found for email: {email}")
        return None

    logger.info(f"Retrieved OTP code for email: {email}")
    return otp_code


def delete_reset_password_otp_code(email: str):
    """
    Delete the OTP code for password reset against the user's email.
    """
    cache_key = f"reset_password_otp_code_{email}"
    cache.delete(cache_key)
    logger.info(f"OTP code for email: {email} has been deleted.")
