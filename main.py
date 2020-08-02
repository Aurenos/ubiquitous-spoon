import asyncio
from random import randint

from node import Node
from topology import Topology


async def main_loop(topology: Topology, tick: int):
    print("Main Loop Started")
    # TODO: listen for graceful exit
    while True:
        await asyncio.sleep(tick)

        node_id = randint(0, topology.size - 1)
        payload = randint(100, 999)
        print(f"Sending {payload} to Node {node_id}")
        topology.send_message(node_id, payload)


async def main(size: int, main_tick: int, node_tick: int):
    top = Topology(size, node_tick)
    await asyncio.gather(
        main_loop(top, main_tick),
        top.start_nodes()
    )

if __name__ == '__main__':
    TOPOLOGY_SIZE = 5
    MAIN_LOOP_TICK = 2
    NODE_TICK = 6

    asyncio.run(
        main(
            TOPOLOGY_SIZE,
            MAIN_LOOP_TICK,
            NODE_TICK
        )
    )
