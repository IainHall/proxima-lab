
import asyncio
import time
async def async_wait(length=5):
    time_started= time.strftime('%X')
    
    await asyncio.sleep(length)
    time_finished= time.strftime('%X')
    print("time_started",time_started, ", waited ",length, ", time finished ", time_finished)
    return time_finished


async def main():

    for i in range(5):
        task1 = asyncio.create_task(async_wait(2))
        task2 = asyncio.create_task(async_wait(1))

        await task1
        await task2

asyncio.run(main())
