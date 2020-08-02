import asyncio
from random import randint

from topology import Topology


async def main_loop(topology: Topology, tick: int):
    print("Main Loop Started")
    # TODO: listen for graceful exit
    while True:
        await asyncio.sleep(tick)

        node_id = randint(0, topology.size - 1)
        payload = randint(100, 999)
        topology.send_message(node_id, payload)

        for n in topology.pool:
            try:
                msg = n.output_queue.get_nowait()
                topology.broadcast_message(msg)
            except asyncio.QueueEmpty:
                pass


async def main(size: int, main_tick: int, node_tick: int):
    top = Topology(size, node_tick)
    await asyncio.gather(
        main_loop(top, main_tick),
        top.start_nodes()
    )

if __name__ == '__main__':
    TOPOLOGY_SIZE = 5
    MAIN_LOOP_TICK = 5
    NODE_TICK = 2

    asyncio.run(
        main(
            TOPOLOGY_SIZE,
            MAIN_LOOP_TICK,
            NODE_TICK
        )
    )
