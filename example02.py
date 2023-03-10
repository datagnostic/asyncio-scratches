import asyncio
import datetime


def anything(i):
    print(i, datetime.datetime.now())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.call_later(2, loop.stop)
    for i in range(1, 10):
        loop.call_soon(anything, i)
    try:
        loop.run_forever()
    finally:
        loop.close()
