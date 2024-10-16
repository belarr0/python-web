import threading
import time

import asyncio
import random

import asyncio
import concurrent.futures
from time import time

import requests
from time import time

# def print_numbers():
#     for i in range(1, 6):
#         print(f"Number: {i}")
#         time.sleep(1)
#
# def print_letters():
#     for letter in 'ABCDE':
#         print(f"Letter: {letter}")
#         time.sleep(1)
#
# # Record the start time
# start_time = time.time()
#
# # Create threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
#
# # Start threads
# thread1.start()
# thread2.start()
#
# # Wait for threads to complete
# thread1.join()
# thread2.join()
#
# # Record the end time
# end_time = time.time()
#
# # Calculate the total execution time
# total_time = end_time - start_time
#
# print("Both threads have finished execution.")
# print(f"Total execution time: {total_time:.2f} seconds")


# async def random_value():
#     print("start task")
#     await asyncio.sleep(1)
#     print("task finished")
#     return random.random()
#
#
# async def main():
#     task = asyncio.create_task(random_value())
#     print("task scheduled")
#     await task
#     print(f"result: {task.result()}")
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


# def blocks(n):
#     counter = n
#     start = time()
#     while counter > 0:
#         counter -= 1
#     return time() - start
#
#
# async def monitoring():
#     while True:
#         await asyncio.sleep(2)
#         print(f'Monitoring {time()}')
#
#
# async def run_blocking_tasks(executor, n):
#     loop = asyncio.get_event_loop()
#     print('waiting for executor tasks')
#     result = await loop.run_in_executor(executor, blocks, n)
#     return result
#
#
# async def main():
#     asyncio.create_task(monitoring())
#     with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#         futures = [run_blocking_tasks(executor, n) for n in [50_000_000, 60_000_000, 70_000_000]]
#         results = await asyncio.gather(*futures)
#         return results
#
#
# if __name__ == '__main__':
#     result = asyncio.run(main())
#     for r in result:
#         print(r)


<<<<<<< HEAD

async def baz() -> str:
    print('Before Sleep')
    await asyncio.sleep(1)
    print('After Sleep')
    return 'Hello world'


async def main():
    r = baz()
    print(r)
    result = await r
    print(result)


if __name__ == '__main__':
    asyncio.run(main())
=======
# urls = ['http://www.google.com', 'http://www.python.org', 'http://duckduckgo.com']
#
# def preview_fetch(url):
#     r = requests.get(url)
#     return url, r.text[:150]
#
#
# if __name__ == '__main__':
#     start = time()
#     for url in urls:
#         r = preview_fetch(url)
#         print(r)
#     print(time() - start)


# import asyncio
# import websockets
#
#
# async def handler(websocket, path):
#     data = await websocket.recv()
#     reply = f"Data recieved as:  {data}!"
#     print(reply)
#     await websocket.send(reply)
#
#
# async def main():
#     async with websockets.serve(handler, "localhost", 8000):
#         await asyncio.Future()  # run forever
#
# if __name__ == '__main__':
#     asyncio.run(main())


print(['item'+ str(i) for i in range(3) if i == 2])


>>>>>>> ca91882c97f29695aec9c6a5bd157e2f7e26c912


