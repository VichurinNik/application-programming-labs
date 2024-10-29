import downloader
import parser
import iterator
from annotation import create_annotation


def main() -> None:
    arg=parser.parser()
    try:
        downloader.download_images(arg.keyword, arg.number, arg.imgdir)
        create_annotation(arg.imgdir,arg.annotation_file)
        my_iterator = iterator.ImageIterator(arg.annotation_file)
        for item in my_iterator:
            print(item)
    except Exception as e:
        print( {e} )


if __name__ == "__main__":
    main()