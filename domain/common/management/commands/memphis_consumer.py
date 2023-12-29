
from __future__ import annotations

from django.core.management.base import BaseCommand

import os
import json
import asyncio

# Memphis
from memphis import Memphis, MemphisError, MemphisConnectError, MemphisHeaderError

# Services
from domain.user.services.user import get_user_by_id
from domain.common.services.resend import send_email

# Django
from asgiref.sync import sync_to_async

import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Runs the Memphis consumer'

    def handle(self, *args, **options):
        self.stdout.write('Starting Memphis consumer...')
        asyncio.run(main())
        self.stdout.write('Memphis consumer has stopped.')

async def main():

    async def msg_handler(msgs, error, context):
        logger.info("Message handler started")
        try:
            for msg in msgs:
                msg_data = json.loads(msg.get_data().decode())
                logger.info("message: %s", msg_data)
                # Events Handler
                if msg_data['event'] == "user_created":
                    logger.info("user_created event")
                    async_get_user_by_id = sync_to_async(get_user_by_id, thread_sensitive=True)
                    user = await async_get_user_by_id(msg_data['data']['user_id'])
                    async_send_email = sync_to_async(send_email, thread_sensitive=True)
                    response = await async_send_email(
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
                # Acknowledge the message
                await msg.ack()
                # Error handling
                if error:
                    logger.error(error)
        except (MemphisError, MemphisConnectError, MemphisHeaderError) as e:
            logger.error(e)
            return
        finally:
            logger.info("Message handler finished")
        
    try:
        logger.info("Initializing Memphis connection...")
        memphis = Memphis()
        await memphis.connect(
            host=os.getenv("MEMPHIS_HOST"), 
            username=os.getenv("MEMPHIS_CONSUMER_USERNAME"), 
            password=os.getenv("MEMPHIS_CONSUMER_PASSWORD"), 
            account_id=os.getenv("MEMPHIS_ACCOUNT_ID")
        )
        logger.info("Memphis connection established.")
        
        logger.info("Setting up Memphis consumer...")
        consumer = await memphis.consumer(
            station_name=os.getenv("MEMPHIS_STATION_NAME"), 
            consumer_name=os.getenv("MEMPHIS_CONSUMER_NAME"), 
            consumer_group=os.getenv("MEMPHIS_CONSUMER_GROUP")
        )
        logger.info("Memphis consumer setup complete.")
        
        logger.info("Starting to consume messages...")
        consumer.consume(msg_handler)
        
        # Keep your main thread alive so the consumer will keep receiving data
        await asyncio.Event().wait()
        
    except (MemphisError, MemphisConnectError) as e:
        logger.error("Error occurred: ", e)
        
    finally:
        logger.info("Closing Memphis connection...")
        await memphis.close()
        logger.info("Memphis connection closed.")
