# Написать программу, которая скачивает изображения с заданных URL-адресов 
# и сохраняет их на диск. 
# Каждое изображение должно сохраняться в отдельном файле, 
# название которого соответствует названию изображения в URL-адресе. 
# Например URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg 
# - Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# - Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# - Программа должна выводить в консоль информацию о времени скачивания каждого изображения 
# и общем времени выполнения программы.


import asyncio
# pip install aiohttp
import aiohttp
import time
import csv
import os.path
import logging

logging.basicConfig(filename="task_9_asyncio.log", encoding="utf-8", level=logging.INFO,)
logger = logging.getLogger()

with open("task_9_url.csv", "r", newline='') as f:
    urls = [str(*line) for line in csv.reader(f)]


async def download(url):
    start_time_download = time.time()
    # headers = {'content-type': 'image/jpeg'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            filename = os.path.basename(url)
            with open('../Task_9/Files/Asyncio/' + filename, "wb") as f:
                f.write(content)
                logger.info(f"Downloaded {url} in {time.time() - start_time_download:.2f} seconds")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    logger.info(f"Downloading all images: {time.time() - start_time:.2f} seconds")
