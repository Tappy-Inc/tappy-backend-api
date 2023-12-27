from __future__ import annotations
import asyncio
import os
from memphis import Memphis, Headers, MemphisError, MemphisConnectError, MemphisHeaderError, MemphisSchemaError


async def main():
    try:
        memphis = Memphis()
        await memphis.connect(host=os.getenv("MEMPHIS_HOST"), username=os.getenv("MEMPHIS_USERNAME"), password=os.getenv("MEMPHIS_PASSWORD"), account_id=os.getenv("MEMPHIS_ACCOUNT_ID"))
        
        producer = await memphis.producer(station_name=os.getenv("MEMPHIS_STATION_NAME"), producer_name=os.getenv("MEMPHIS_PRODUCER_NAME")) # you can send the message parameter as dict as well
        
        headers = Headers()
        headers.add("<key>", "<value>")
    
        for i in range(5):
            await producer.produce(bytearray("Message #" + str(i) + ": Hello world", "utf-8"), headers=headers)
        
    except (MemphisError, MemphisConnectError, MemphisHeaderError, MemphisSchemaError) as e:
        print(e)
        
    finally:
        await memphis.close()
        
if __name__ == "__main__":
    asyncio.run(main())