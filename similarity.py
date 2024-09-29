import cv2
import scipy.spatial.distance as dist
import numpy as np

def image_similarity(image1_path, image2_path):
	image1 = cv2.imread(image1_path)
	image2 = cv2.imread(image2_path)

	# Check if images are loaded correctly
	if image1 is None:
		print(f"Error loading image: {image1_path}")
	if image2 is None:
		print(f"Error loading image: {image2_path}")

	# Resize images to the same dimensions
	target_size = (224, 224)  # Example target size
	image1_resized = cv2.resize(image1, target_size)
	image2_resized = cv2.resize(image2, target_size)

	# Flatten the images
	image1_flattened = image1_resized.flatten()
	image2_flattened = image2_resized.flatten()

	# Compute Euclidean distance
	a = dist.euclidean(image1_flattened, image2_flattened)
	return a / 100000  # 0 ==> similar image, 1 ==> different image