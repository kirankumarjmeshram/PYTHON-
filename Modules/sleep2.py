import asyncio
import time

async def output(sleep, text):
    await asyncio.sleep(sleep)
    print(text)

async def main():
    print(f"Started: {time.strftime('%X')}")
    await output(4, 'First')
    await output(2, 'Second')
    await output(1, 'Third')
    print(f"Ended: {time.strftime('%X')}")

# Python 3.7+
asyncio.run(main())

# Started: 11:06:55
# First
# Second
# Third
# Ended: 11:07:02