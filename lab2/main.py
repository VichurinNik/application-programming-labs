import downloader
import parser
import iterator
from annotation import annotation


def main() -> None:
    arg=parser.parser()
    try:
        downloader.download(arg.keyword, arg.number, arg.imgdir)
        annotation(arg.imgdir,arg.annotation_file)
        my_iterator = iterator.ImageIterator(arg.annotation_file)
        for item in my_iterator:
            print(item)
    except Exception as e:
        print( {e} )


if __name__ == "__main__":
    main()