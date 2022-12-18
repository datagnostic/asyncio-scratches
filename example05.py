import asyncio

from example04 import anything

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(anything(i)) for i in range(1, 4)]
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    finally:
        loop.close()
