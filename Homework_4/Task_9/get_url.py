import requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import csv

image_sources = []

# URL = "imagesiteURL" # Replace this with the website's URL
for i in range(6):
    URL = f"https://ru.wallpaper.mob.org/gallery/tag=oshki_oty_otiki/{i}/"
    get_url = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
    print(get_url.status_code)

    soup = BeautifulSoup(get_url.text, 'html.parser')
    images = soup.find_all('img')

    for image in images:
        image_sources.append(image.get('src'))

spam = set(image_sources)
urls = list(spam)

with open("task_9_url.csv", "w", newline='') as f:
    csv_write = csv.writer(f)
    [csv_write.writerow([url]) for url in urls]
