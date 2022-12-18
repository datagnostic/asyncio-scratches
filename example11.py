import asyncio
import datetime
import math
import time
from concurrent.futures import ThreadPoolExecutor


def is_prime(n):
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def function(i: int) -> tuple[int, datetime.datetime]:
    started_time = datetime.datetime.now()
    print(f"function {i} has started at {started_time}")
    is_prime(1099726899285419)
    finished_time = datetime.datetime.now()
    print(f"function {i} has finished at {finished_time}")
    return i, finished_time


async def consume(running_functions: asyncio.Queue, max_consumption: int):
    futures_function = await running_functions.get()
    result = await futures_function
    print(f"function {result[0]} reported at " f"{datetime.datetime.now()}")
    if result[0] == max_consumption:
        return
    await consume(running_functions, max_consumption)


async def function_execution(loop, i, executor, running_functions):
    future = loop.run_in_executor(executor, function, i)
    await running_functions.put(future)


async def main(executor):
    queue = asyncio.Queue()
    number_of_products = 8
    loop = asyncio.get_event_loop()
    consumer = asyncio.create_task(consume(queue, number_of_products))
    producers = [
        asyncio.create_task(function_execution(loop, i, executor, queue))
        for i in range(1, number_of_products + 1)
    ]
    await asyncio.gather(*producers, consumer)


if __name__ == "__main__":
    start_time = time.time()
    with ThreadPoolExecutor() as e:
        asyncio.run(main(e))
    print("Script execution time: ", time.time() - start_time)
