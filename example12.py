import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

from example11 import main

if __name__ == "__main__":
    start_time = time.time()
    with ProcessPoolExecutor() as e:
        asyncio.run(main(e))
    print("Script execution time: ", time.time() - start_time)
