import asyncio
import itertools
from typing import Any


class Node(object):
    new_id = itertools.count()

    def __init__(self, tick: int):
        self._id = next(Node.new_id)
        self.tick = tick
        self.input_queue = asyncio.Queue()
        self.output_queue = asyncio.Queue()

    async def run(self):
        while True:
            await asyncio.sleep(self.tick)
            # print(f'\t{self} is still running')

            item = self.recv()
            if item:
                print(f"\t{self} got {item}")

                if item % 2 == 0:
                    self.send(6969)

    def recv(self):
        try:
            item = self.input_queue.get_nowait()
            return item
        except asyncio.QueueEmpty:
            pass

    def send(self, msg: Any):
        try:
            self.output_queue.put_nowait(msg)
        except asyncio.QueueFull:
            pass

    def __str__(self):
        return f'<Node {str(self._id)}>'

    def __repr__(self):
        return f'<Node {str(self._id)}>'
