import requests
from multiprocessing import Process
import time
from app import urls


def download_images(url):
    response = requests.get(url)
    filename = "multiprocessing_"+url.replace("https://", "").split("/")[-1]
    with open(f"../dz4/images/{filename}", "wb") as f:
        f.write(response.content)
    print(f"Скачано за {url} in {time.time() - start_time:.2f} сек.")


processes = []
start_time = time.time()
if __name__ == "__main__":
    for url in urls:
        process = Process(target=download_images, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
