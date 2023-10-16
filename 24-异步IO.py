import asyncio
from threading import current_thread


async def f1():
    print("f1 start", current_thread())
    await asyncio.sleep(1)
    print("f1 end", current_thread())


async def f2():
    print("f2 start", current_thread())
    await asyncio.sleep(1)
    print("f2 end", current_thread())


tasks = [
    asyncio.create_task(f1()),
    asyncio.create_task(f2())
]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(*tasks))
asyncio.run(asyncio.wait(tasks))

