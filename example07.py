import asyncio

from example06 import anything

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = loop.create_task(anything(3))
    try:
        result = loop.run_until_complete(task)
        print(*result)
    finally:
        loop.close()
