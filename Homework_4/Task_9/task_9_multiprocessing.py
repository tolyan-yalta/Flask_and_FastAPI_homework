# Написать программу, которая скачивает изображения с заданных URL-адресов 
# и сохраняет их на диск. 
# Каждое изображение должно сохраняться в отдельном файле, 
# название которого соответствует названию изображения в URL-адресе. 
# Например URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg 
# - Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# - Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# - Программа должна выводить в консоль информацию о времени скачивания каждого изображения 
# и общем времени выполнения программы.

import requests
import multiprocessing
import time
import csv
import os.path
import logging

logging.basicConfig(filename="task_9_multiprocessing.log", encoding="utf-8", level=logging.INFO,)
logger = logging.getLogger()

with open("task_9_url.csv", "r", newline='') as f:
    urls = [str(*line) for line in csv.reader(f)]


def download(url):
    start_time_download = time.time()
    response = requests.get(url)
    filename = os.path.basename(url)
    with open('../Task_9/Files/Multiprocessing/' + filename, "wb") as f:
        f.write(response.content)
        logger.info(f"Downloaded {url} in {time.time() - start_time_download:.2f} seconds")


if __name__ == "__main__":
    processes = []
    start_time = time.time()
    for url in urls:
        process = multiprocessing.Process(target=download, args=[url])
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    logger.info(f"Downloading all images: {time.time() - start_time:.2f} seconds")
