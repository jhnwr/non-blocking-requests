# "threading is for working in parallel, and async is for waiting in parallel".
import requests
from time import perf_counter

start = perf_counter()


for x in range(1, 25000):
    r = requests.get(f'http://127.0.0.1:8000/items/{x}')
    print(r.json())

stop = perf_counter()
print("time taken:", stop - start)
# time taken: 58.477935733004415