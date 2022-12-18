import asyncio
import datetime


async def anything(i):
    print(i, datetime.datetime.now())
    try:
        await asyncio.sleep(i)
    except TypeError:
        i = 0
    return i, datetime.datetime.now()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = loop.create_task(anything("g"))
    try:
        result = loop.run_until_complete(task)
        print(*result)
    finally:
        loop.close()
