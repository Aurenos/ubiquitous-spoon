import asyncio

from node import Node


async def main():
    print("Main!")

    pool = list()

    for _ in range(5):
        pool.append(Node())

    print("Pool initialized")

    await asyncio.gather(*[n.do_action() for n in pool])

    print("Main ended")


if __name__ == '__main__':
    asyncio.run(main())
