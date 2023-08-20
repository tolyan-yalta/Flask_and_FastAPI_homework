import asyncio
import time
import random

res = 0


async def sum_item(list_):
    global res
    res_sum = 0
    for i in list_:
        res_sum =  res_sum + i
    res +=  res_sum


async def method_asinc(arr):
    list_index = [[0, 25_000_000], [25_000_000, 50_000_000], [50_000_000, 75_000_000], [75_000_000, 100_000_000]]
    start_time = time.time()
    tasks = []
    for indexs in list_index:
        list_ = arr[indexs[0]:indexs[1]]
        task = asyncio.ensure_future(sum_item(list_))
        tasks.append(task)
    await asyncio.gather(*tasks)

    print(f'Method asyncio: time - {time.time() - start_time:.5f} sec.')
    print(res)

if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(1_000_000)]
    asyncio.run(method_asinc(arr))
    pass
