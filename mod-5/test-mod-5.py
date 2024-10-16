import time
import asyncio

def first():
    print("First thing")
    time.sleep(3)
    print("End first thing")

def second():
    print("Second thing")
    time.sleep(2)
    print("End second thing")


async def first_async():
    print("First thing")
    await asyncio.sleep(3)
    print("End first thing")

async def second_async():
    print("Second thing")
    await asyncio.sleep(2)
    print("End second thing")


async def main_async():
    await asyncio.gather(first_async(), second_async())


if __name__ == '__main__':
    start = time.time()

    first()
    second()

    print(f"{(time.time() - start):.2f}")
    print("----------------")

    start = time.time()

    asyncio.run(main_async())

    print(f"{(time.time() - start):.2f}")
