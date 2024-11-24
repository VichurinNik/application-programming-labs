import image
import schedule
import parser


def main():
	arg = parser.parser()
	try:
		img1 = image.read_image(arg.image1)
		img2 = image.read_image(arg.image2)
		print(f"Image size 1: {img1.shape}")
		print(f"Image size 2: {img2.shape}")
		b, g, r = schedule.histogram_of_channels(img1)
		schedule.show_hist(b, g, r)

		combined = image.combined_images(img1, img2)

		image.display_img(img1, "Image1")
		image.display_img(img2,"Image2")
		image.display_img(combined, "Combinet Images")

		image.save_image(combined, arg.output)
	except Exception as e:
		print(e)


if __name__ == "__main__":
	main()