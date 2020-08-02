import asyncio
import itertools


class Node(object):
    new_id = itertools.count()

    def __init__(self, tick: int):
        self._id = next(Node.new_id)
        self.tick = tick
        self.input_queue = asyncio.Queue()

    async def run(self):
        while True:
            await asyncio.sleep(self.tick)
            # print(f'\t{self} is still running')

            item = self.recv()
            if item:
                print(f"\t{self} got {item}")

    def recv(self):
        try:
            item = self.input_queue.get_nowait()
            return item
        except asyncio.QueueEmpty:
            pass

    def __str__(self):
        return f'<Node {str(self._id)}>'

    def __repr__(self):
        return f'<Node {str(self._id)}>'
