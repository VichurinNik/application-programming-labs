import os

from icrawler.builtin import GoogleImageCrawler


def download(keyword: str, number: int, imgdir: str) -> None:
    """
    It is used to download images by keyword using the Bing Image Crawler library.
    It accepts three parameters: keyword for search, number
    for limiting the number of uploaded images, and imgdir for specifying the save directory.
    """
    for filename in os.listdir(imgdir):
        os.remove(os.path.join(imgdir, filename))

    my_crawler = GoogleImageCrawler(
        storage={"root_dir": imgdir, "backend": "FileSystem"},
        feeder_threads=2,
        parser_threads=2,
        downloader_threads=8)

    my_crawler.crawl(keyword=keyword, max_num=number)

