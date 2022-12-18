import asyncio
import datetime
import time


def anything(i):
    print(i, datetime.datetime.now())
    time.sleep(i)


if __name__ == "__main__":
    """set PYTHONASYNCIODEBUG=1"""
    loop = asyncio.get_event_loop()
    loop.call_later(2, loop.stop)
    for i in range(1, 10):
        loop.call_soon(anything, i)
    try:
        loop.run_forever()
    finally:
        loop.close()
