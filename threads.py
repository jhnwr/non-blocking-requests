from concurrent.futures import ThreadPoolExecutor

from time import perf_counter

start = perf_counter()

import requests

urls = range(1, 5000)


def get_data(url):
    r = requests.get(f'http://127.0.0.1:8000/items/{url}')
    print(r.json())


with ThreadPoolExecutor(max_workers=12) as executor:
    executor.map(get_data, urls)

stop = perf_counter()
print("time taken:", stop - start)
