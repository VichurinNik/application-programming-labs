import argparse

def parser() -> argparse.Namespace:
	"""
	Creates an ArgumentParser object and adds command line arguments.
	    Parses the arguments entered by the user and returns a Namespace with the results.

	    :return: A Namespace object containing the values of the command-line arguments
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument("-1i", "--image1",default="D:\laba3\laba3\image\Image1.jpg", type=str, help="The path to 1 image file")
	parser.add_argument("-2i", "--image2",default="D:\laba3\laba3\image\image2.jpg", type=str, help="The path to 2 image file")
	parser.add_argument("-n","--output", default="D:\\laba3\\laba3\\image", type=str, help="The path to save the image")
	arguments = parser.parse_args()
	return arguments