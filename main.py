import asyncio
from typing import List

from node import Node


async def main():
    print("Main!")

    pool: List[Node] = list()

    for _ in range(5):
        pool.append(Node())

    print("Pool initialized")

    await asyncio.gather(*[n.do_action() for n in pool])

    print("Main ended")


if __name__ == '__main__':
    asyncio.run(main())
