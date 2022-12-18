import asyncio
import datetime


async def inside_coroutine(i):
    print("inside coroutine", i, datetime.datetime.now())
    await asyncio.sleep(i)
    return i, datetime.datetime.now()


async def anything(i):
    result = await inside_coroutine(i)
    print("coroutine", result)
    return result


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(anything(i)) for i in range(1, 4)]
    try:
        loop.run_until_complete(asyncio.wait(tasks))
        for task in tasks:
            print(*task.result())
    finally:
        loop.close()
