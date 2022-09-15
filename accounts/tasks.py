from asyncio.log import logger
from celery.decorators import task
from celery.utils.log import get_task_logger
from accounts.services.emails.user_email import UserEmailService

logger = get_task_logger(__name__)
@task(name="send_activate_email")
def send_activate_email(current_site, user_id, to_email):
    logger.info("Sending activate email")
    return UserEmailService.send_activate_email(current_site, user_id, to_email)