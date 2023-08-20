import threading
import time
import random

res = 0


def sum_item(list_):
    global res
    res_sum = 0
    for i in list_:
        res_sum += i
    res +=  res_sum


def method_threading(arr):
    list_index = [[0, 25_000_000], [25_000_000, 50_000_000], [50_000_000, 75_000_000], [75_000_000, 100_000_000]]
    start_time = time.time()
    threads = []
    for indexs in list_index:
        list_ = arr[indexs[0]:indexs[1]]
        t = threading.Thread(target=sum_item, args=(list_, ))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f'Method threading: time - {time.time() - start_time:.5f} sec.')
    print(res)


if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(100_000_000)]
    method_threading(arr)
    pass
