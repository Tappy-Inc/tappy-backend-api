from __future__ import annotations

import os
import json

# Memphis
from memphis import Memphis, Headers, MemphisError, MemphisConnectError, MemphisHeaderError, MemphisSchemaError

import logging
logger = logging.getLogger(__name__)


async def create_message(payload: dict):
    try:
        memphis = Memphis()
        await memphis.connect(
            host=os.getenv("MEMPHIS_HOST"), 
            username=os.getenv("MEMPHIS_PRODUCER_USERNAME"), 
            password=os.getenv("MEMPHIS_PRODUCER_PASSWORD"), 
            account_id=os.getenv("MEMPHIS_ACCOUNT_ID")
        )
        producer = await memphis.producer(
            station_name=os.getenv("MEMPHIS_STATION_NAME"), 
            producer_name=os.getenv("MEMPHIS_PRODUCER_NAME")
        )  
        headers = Headers()

        await producer.produce(bytearray(json.dumps(payload), "utf-8"), headers=headers)
        
    except (MemphisError, MemphisConnectError, MemphisHeaderError, MemphisSchemaError) as e:
        logger.error(e)
        
    finally:
        await memphis.close()
