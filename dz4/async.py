
import asyncio
import aiohttp
import time
from app import urls


async def download_images(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            image = await response.read()
            filename = "async_"+url.replace("https://", "").split("/")[-1]
        with open(f"../dz4/images/{filename}", "wb") as f:
            f.write(image)
            print(f"Скачано за {url} in {time.time() - start_time:.2f} сек.")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_images(url))
        tasks.append(task)
        await asyncio.gather(*tasks)


start_time = time.time()
if __name__ == "__main__":
    asyncio.run(main())
