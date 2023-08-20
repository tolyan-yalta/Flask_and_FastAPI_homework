import multiprocessing
import time
import random

res = multiprocessing.Value("q", 0)


def sum_item(list_, val):
    res_sum = 0
    for i in list_:
        res_sum += i
    with val.get_lock():
        val.value += res_sum


def method_multiprocessing(arr):
    list_index = [[0, 25_000_000], [25_000_000, 50_000_000], [50_000_000, 75_000_000], [75_000_000, 100_000_000]]
    start_time = time.time()
    processes = []
    
    for indexs in list_index:
        list_ = arr[indexs[0]:indexs[1]]
        process = multiprocessing.Process(target=sum_item, args=(list_, res))
        processes.append(process)
        process.start()

    [process.join() for process in processes]
        
    print(f'Method multiprocessing: time - {time.time() - start_time:.5f} sec.')
    print(res.value)


if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(100_000_000)]
    method_multiprocessing(arr)
    pass
