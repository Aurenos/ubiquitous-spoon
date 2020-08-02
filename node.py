import asyncio
import itertools


class Node(object):
    new_id = itertools.count()

    def __init__(self):
        self._id = next(Node.new_id)
        self.num_q = asyncio.Queue()

    async def run(self):
        while True:
            await asyncio.sleep(2)
            print(f'\t{self} is still running')
            try:
                item = self.num_q.get_nowait()
                print(f"{self} got {item}")
            except asyncio.QueueEmpty:
                pass

    def __str__(self):
        return f'<Node {str(self._id)}>'

    def __repr__(self):
        return f'<Node {str(self._id)}>'
