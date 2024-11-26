import argparse


def parser() -> argparse.Namespace:
    """
    Reads arguments from terminal
    :return: Argumentsss
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--annotation_file',default="D:\Laba2\lab2\\annotation.csv" ,type=str, help='Путь к файлу для аннотации')
    parser.add_argument('-mw', '--max_width', type=int, default=1920, help='Максимальная ширина')
    parser.add_argument('-mh', '--max_height', type=int,default=1080, help='Максимальная высота')
    arguments = parser.parse_args()
    return arguments