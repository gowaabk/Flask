# Урок 4. Введение в многозадачность

# Задание

# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.

# запуск "python app.py m" для - Multiprocessing
# запуск "python app.py a" для - async
# запуск "python app.py t" для - Threadings

import os
import sys
import argparse


urls = [
    "https://sportishka.com/uploads/posts/2022-04/1651196991_22-sportishka-com-p-mnogo-mashin-mashini-krasivo-foto-28.jpg",
    "https://sportishka.com/uploads/posts/2021-12/1639055646_1-sportishka-com-p-sovremennie-mashini-sport-krasivo-foto-1.jpg",
    "https://pit-lyubimchik.ru/wp-content/uploads/2022/06/cf369eb74b5d6d9a6f3c8e30690bbe9e.jpeg-raznye-sobaki.jpeg",
    "https://krasivosti.pro/uploads/posts/2022-08/1661351156_22-krasivosti-pro-p-vsyakie-porodi-sobak-sobaki-30.jpg"

]

if __name__ == "__main__":
    file_name = ""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "value", nargs='?', help="Input: python app.py a(for async), t(for threading) ,m(for Multiprocessing)")
    args = parser.parse_args()
    # print(args.value)
    # print(args)
    match args.value:
        case "a":
            file_name = "python async.py"
        case "t":
            file_name = "python threadings.py"
        case "m":
            file_name = "python multiprocess.py"
        case _:
            print("Не верный параметр")
    # print(file_name)
    if args.value:
        os.system(f"{file_name}")
