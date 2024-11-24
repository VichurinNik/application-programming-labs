import matplotlib.pyplot as plt
import cv2
import numpy as np


def histogram_of_channels(img: np.ndarray) -> tuple:
	"""
	Calculates the histograms of each channel (BGR) of the image and returns them.

	    :param img: Image in ndarray format
	:return: Three lists of histogram values for each channel (B, G, R)
	"""
	blue = cv2.calcHist([img], [0], None, [256], [0, 255])
	green = cv2.calcHist([img], [1], None, [256], [0, 255])
	red = cv2.calcHist([img], [2], None, [256], [0, 255])
	return blue, green, red


def show_hist(blue: np.ndarray, green: np.ndarray, red:  np.ndarray) -> None:
	"""
	Plots histograms for each channel (BGR) of the image.

	    :param blue: Histogram of the blue channel
	:param green: Histogram of the green channel
	:param red: Histogram of the red channel
	"""
	plt.figure(figsize=(10, 5))
	plt.plot( blue, label='Синяя линия', color='blue')
	plt.plot( green, label='Зеленая линия', color='green')
	plt.plot( red, label='Красная линия', color='red')
	plt.xlim([0, 255])
	plt.title('Гистограмма цвета изображения')
	plt.xlabel('Интенсивность цвета')
	plt.ylabel('Частота')
	plt.grid()
	plt.legend()
	plt.show()