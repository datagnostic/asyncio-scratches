import asyncio

from example06 import anything

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = loop.create_task(anything('g'))
    try:
        result = loop.run_until_complete(task)
    except TypeError:
        print("Type error: ", task.exception())
    else:
        print(*result)
    finally:
        loop.close()
