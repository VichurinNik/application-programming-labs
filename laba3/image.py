import cv2
import numpy as np
import os


def read_image(file_name) -> np.ndarray:
	"""
	Reads an image from a file and returns it as a NumPy array.

	    :param file_name: Path to the image file
	:return: Image in ndarray format
	"""
	img = cv2.imread(file_name)
	return img


def display_img(img,title)->None:
	"""
	Displays the image in a new window with the specified title.

	    :param img: Image in ndarray format
	:param title: Window title
	"""
	cv2.imshow(title, img )
	cv2.waitKey(0)


def combined_images(img1, img2)->np.ndarray:
	"""
	Combines two images horizontally and returns the result.

	    :param img1: First image in ndarray format
	:param img2: Second image in ndarray format
	:return: Combined image in ndarray format
	"""
	combined_image = np.concatenate((img1, img2), axis=1)
	return combined_image


def save_image(image, output)->None:
	"""
	Saves the image in the specified directory.

	    :param image: Image in ndarray format
	:param output: Directory for saving the image
	"""
	os.chdir(output)
	print(os.listdir(output))
	cv2.imwrite('combined_img.png', image)









