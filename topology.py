import asyncio
from typing import Any, List
from node import Node


class Topology:
    def __init__(self, size: int, node_tick: int = 1):
        self.size = size
        self.pool: List[Node] = []

        for _ in range(size):
            self.pool.append(Node(node_tick))

    async def start_nodes(self):
        await asyncio.gather(*(n.run() for n in self.pool))

    def _get_node_by_id(self, node_id: int):
        return next((n for n in self.pool if n._id == node_id), None)

    def send_message(self, node_id: int, message: Any):
        node = self._get_node_by_id(node_id)
        if not node:
            raise Exception("That ID doesn't exist")

        node.input_queue.put_nowait(message)
