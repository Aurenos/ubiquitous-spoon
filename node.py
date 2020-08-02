import asyncio
import itertools


class Node(object):
    new_id = itertools.count()

    def __init__(self):
        self._id = next(Node.new_id)

    async def run(self):
        while True:
            await asyncio.sleep(5)
            print(f"{self} performed action")

    def __str__(self):
        return f'<Node {str(self._id)}>'

    def __repr__(self):
        return f'<Node {str(self._id)}>'
