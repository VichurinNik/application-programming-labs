import argparse

def parser() -> argparse.Namespace:
    """
    Reads arguments from terminal
    :return: Arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="Keyword of search request")
    parser.add_argument("-n", "--number", type=int, default=50,  help="Number of images that you want to download (default: 2)")
    parser.add_argument("-d", "--imgdir", type=str, default="D:\Laba2\lab2\images", help="Path to the folder, where you want to save images ")
    parser.add_argument("-f", "--annotation_file", type=str, default="D:\\Laba2\lab2\\annotation.csv", help="Path to the annotation file")
    arguments = parser.parse_args()
    return arguments