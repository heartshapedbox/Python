import asyncio

async def x():
    print("Hello ")
    await asyncio.sleep(3)
    print("World!")

asyncio.run(x())
