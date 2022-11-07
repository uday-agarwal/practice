'''asyncio is a library to write concurrent code using async/await syntax

Good for I/O bound and high-level structured network code.
'''

import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())
