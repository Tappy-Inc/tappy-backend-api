from __future__ import annotations

import os
import json

# Django
import django
from asgiref.sync import sync_to_async

import logging
logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tappy.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

# Events
from events.mailer import send_welcome_email

# Memphis
import asyncio
from memphis import Memphis, MemphisError, MemphisConnectError, MemphisHeaderError


async def main():

    async def msg_handler(msgs, error, context):
        try:
            for msg in msgs:
                msg_data = json.loads(msg.get_data().decode())
                logger.info("message: %s", msg_data)
                # Events Handler
                if msg_data['event'] == "user_created":
                    async_send_welcome_email = sync_to_async(send_welcome_email, thread_sensitive=True)
                    response = await async_send_welcome_email(msg_data['data']['user_id'])
                    logger.info(response)
                # Acknowledge the message
                await msg.ack()
                # Error handling
                if error:
                    logger.error(error)
        except (MemphisError, MemphisConnectError, MemphisHeaderError) as e:
            logger.error(e)
            return
        
    try:
        memphis = Memphis()
        await memphis.connect(
            host=os.getenv("MEMPHIS_HOST"), 
            username=os.getenv("MEMPHIS_CONSUMER_USERNAME"), 
            password=os.getenv("MEMPHIS_CONSUMER_PASSWORD"), 
            account_id=os.getenv("MEMPHIS_ACCOUNT_ID")
        )
        
        consumer = await memphis.consumer(
            station_name=os.getenv("MEMPHIS_STATION_NAME"), 
            consumer_name=os.getenv("MEMPHIS_CONSUMER_NAME"), 
            consumer_group=os.getenv("MEMPHIS_CONSUMER_GROUP")
        )
        
        consumer.consume(msg_handler)
        
        # Keep your main thread alive so the consumer will keep receiving data
        await asyncio.Event().wait()
        
    except (MemphisError, MemphisConnectError) as e:
        logger.error(e)
        
    finally:
        await memphis.close()
        
if __name__ == "__main__":
    asyncio.run(main())