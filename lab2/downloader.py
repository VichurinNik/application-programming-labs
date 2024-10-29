import os

from icrawler.builtin import GoogleImageCrawler

def download(keyword: str, number: int, imgdir: str) -> None:
    for filename in os.listdir(imgdir):
        """
        Deletes old images from the target directory before uploading new ones.
        """
        os.remove(os.path.join(imgdir, filename))
        """
        A function for uploading images using the Google Image Crawler library.
        """
    my_crawler = GoogleImageCrawler(
    storage={"root_dir": imgdir, "backend": "FileSystem"},
    feeder_threads=2,
    parser_threads=2,
    downloader_threads=8)
    my_crawler.crawl(keyword=keyword, max_num=number)