import asyncio
from typing import List

from node import Node

TOPOLOGY_SIZE = 5


class Topology:
    def __init__(self, size):
        self.pool: List[Node] = []

        for _ in range(size):
            self.pool.append(Node())

    async def start_nodes(self):
        await asyncio.gather(*(n.run() for n in self.pool))


async def main_loop(topology: Topology):
    print("Main Loop Started")
    # TODO: listen for graceful exit
    # asdfpP
    while True:
        await asyncio.sleep(5)
        print("Main tick")


async def main(size: int):
    top = Topology(size)
    await asyncio.gather(
        main_loop(top),
        top.start_nodes()
    )

if __name__ == '__main__':
    asyncio.run(main(TOPOLOGY_SIZE))
