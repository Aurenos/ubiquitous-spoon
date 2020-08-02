import asyncio
from uuid import uuid1


class Node(object):
    def __init__(self):
        self._id = uuid1()

    async def do_action(self):
        while True:
            await asyncio.sleep(5)
            print(f"{self} performed action")

    def __str__(self):
        return f'<Node {str(self._id)}>'

    def __repr__(self):
        return f'<Node {str(self._id)}>'
