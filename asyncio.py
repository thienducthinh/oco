import asyncio

async def background_task():
    print("Background task started")
    await asyncio.sleep(3)
    print("Background task finished")

async def main():
    task = asyncio.create_task(background_task())  # Runs in the background
    print("Main function is running")
    await asyncio.sleep(1)  # Simulating other work
    print("Main function finished")
    await task  # Ensure background task completes before exiting

asyncio.run(main())