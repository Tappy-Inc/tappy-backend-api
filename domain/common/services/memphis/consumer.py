from __future__ import annotations
import asyncio
import os
from memphis import Memphis, MemphisError, MemphisConnectError, MemphisHeaderError


async def main():
    async def msg_handler(msgs, error, context):
        try:
            for msg in msgs:
                print("message: ", msg.get_data())
                await msg.ack()
                if error:
                    print(error)
        except (MemphisError, MemphisConnectError, MemphisHeaderError) as e:
            print(e)
            return
        
    try:
        memphis = Memphis()
        await memphis.connect(host=os.getenv("MEMPHIS_HOST"), username=os.getenv("MEMPHIS_USERNAME"), password=os.getenv("MEMPHIS_PASSWORD"), account_id=os.getenv("MEMPHIS_ACCOUNT_ID"))
        
        consumer = await memphis.consumer(station_name=os.getenv("MEMPHIS_STATION_NAME"), consumer_name=os.getenv("MEMPHIS_CONSUMER_NAME"), consumer_group=os.getenv("MEMPHIS_CONSUMER_GROUP"))
        consumer.set_context({"key": "value"})
        consumer.consume(msg_handler)
        # Keep your main thread alive so the consumer will keep receiving data
        await asyncio.Event().wait()
        
    except (MemphisError, MemphisConnectError) as e:
        print(e)
        
    finally:
        await memphis.close()
        
if __name__ == "__main__":
    asyncio.run(main())