import asyncio
from time import perf_counter

import aiohttp


async def fetch(s, url):
    async with s.get(f'http://127.0.0.1:8000/items/{url}') as r:
        if r.status != 200:
            r.raise_for_status()
        return await r.text()


async def fetch_all(s, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(s, url))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res


async def main():
    urls = range(1, 25000)
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_all(session, urls)
        print(htmls)


if __name__ == '__main__':
    start = perf_counter()
    asyncio.run(main())
    stop = perf_counter()
    print("time taken:", stop - start)
    # time taken: 14.692326207994483
