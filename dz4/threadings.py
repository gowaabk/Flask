import requests
import time
import threading
from app import urls


def download_images(url):
    response = requests.get(url)
    filename = "threading_"+url.replace("https://", "").split("/")[-1]
    with open(f"../dz4/images/{filename}", "wb") as f:
        f.write(response.content)
    print(f"Скачано за {url} in {time.time() - start_time:.2f} сек.")


threads = []
start_time = time.time()

if __name__ == "__main__":
    for url in urls:
        thread = threading.Thread(target=download_images, args=[url])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()