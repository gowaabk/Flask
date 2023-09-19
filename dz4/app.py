# Урок 4. Введение в многозадачность

# Задание

# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.

# запуск python app.py -url {имя файла}.py

import os
import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-url", help=" Пример: python app.py -url {имя файла}.py")
    return parser


urls = [
    "https://sportishka.com/uploads/posts/2022-04/1651196991_22-sportishka-com-p-mnogo-mashin-mashini-krasivo-foto-28.jpg",
    "https://sportishka.com/uploads/posts/2021-12/1639055646_1-sportishka-com-p-sovremennie-mashini-sport-krasivo-foto-1.jpg",
    "https://pit-lyubimchik.ru/wp-content/uploads/2022/06/cf369eb74b5d6d9a6f3c8e30690bbe9e.jpeg-raznye-sobaki.jpeg",
    "https://krasivosti.pro/uploads/posts/2022-08/1661351156_22-krasivosti-pro-p-vsyakie-porodi-sobak-sobaki-30.jpg"

]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", nargs="?", help="Multiprocessing")
    parser.add_argument("-t", help="Threadings")
    parser.add_argument("-a", help="Async")
    args = parser.parse_args()
    print(args.m)
    # match namespace:
    #     case <pattern_1>:
    #         <action_1>
    #     case <pattern_2>:
    #         <action_2>
    #     case <pattern_3>:
    #         <action_3>
    #     case _:
    #         <action_wildcard>
    # os.system(f"python {namespace.url}")
