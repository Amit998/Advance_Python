import asyncio

async def main():
    task=asyncio.create_task(other_function())
    print("A")
    # await other_function()
    # await task
    await asyncio.sleep(1)
    print("B")
    return_value=await task
    print(f"Return Value was {return_value}")
    # await task

async def other_function():
    print("1")
    await  asyncio.sleep(2)
    print("2")
    return 10

asyncio.run(main())