# Задание №7
# * Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# * Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# * Массив должен быть заполнен случайными целыми числами от 1 до 100.
# * При решении задачи нужно использовать 
# многопоточность, многопроцессорность и асинхронность.
# * В каждом решении нужно вывести время выполнения вычислений.

from task_7_threading import method_threading
from task_7_multiprocessing import method_multiprocessing
from task_7_async import method_asinc
import asyncio
import time
import random


def sum_item(arr):
    start_time = time.time()
    res = 0
    for i in arr:
        res += i
    print(f'Method synchronous: time - {time.time() - start_time:.5f} sec.')
    print(res)


if __name__ == '__main__':
    start_time = time.time()
    arr = [random.randint(1, 100) for _ in range(100_000_000)]
    print(f'Fill array: time - {time.time() - start_time:.5f} sec.')
    sum_item(arr)
    method_threading(arr)
    method_multiprocessing(arr)
    asyncio.run(method_asinc(arr))

# Fill array: time - 109.07718 sec.
# Method synchronous: time - 7.84497 sec.
# 5050174140
# Method threading: time - 6.64570 sec.
# 5050174140
# Method multiprocessing: time - 10.34891 sec.
# 5050174140
# Method asyncio: time - 7.61779 sec.
# 5050174140