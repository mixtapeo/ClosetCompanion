import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0' 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
from tensorflow import keras
from keras import applications
import sql
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from PIL import Image as PILImage
import glob
import cv2
import scipy.spatial.distance as dist
import numpy as np

# # Old model, deprecated.
# def image_similarity(image1_path, image2_path):
# 	image1 = cv2.imread(image1_path)
# 	image2 = cv2.imread(image2_path)

# 	# Check if images are loaded correctly
# 	if image1 is None:
# 		print(f"Error loading image: {image1_path}")
# 	if image2 is None:
# 		print(f"Error loading image: {image2_path}")

# 	# Resize images to the same dimensions
# 	target_size = (224, 224)  # Example target size
# 	image1_resized = cv2.resize(image1, target_size)
# 	image2_resized = cv2.resize(image2, target_size)

# 	# Flatten the images
# 	image1_flattened = image1_resized.flatten()
# 	image2_flattened = image2_resized.flatten()

# 	# Compute Euclidean distance
# 	a = dist.euclidean(image1_flattened, image2_flattened)
# 	return a / 100000  # 0 ==> similar image, 1 ==> different image


def is_image_similar(img1_path, img2_path, threshold=0.75):
    # Load images
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)
    
    # Check if images are loaded
    if img1 is None or img2 is None:
        print("Error loading images.")
        return False

    # Initialize ORB detector
    orb = cv2.ORB_create()

    # Find keypoints and descriptors with ORB
    keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

    # Initialize BFMatcher (Brute Force Matcher)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors
    matches = bf.match(descriptors1, descriptors2)

    # Sort matches based on distance (lower distance is better)
    matches = sorted(matches, key=lambda x: x.distance)

    # Calculate the similarity score based on the matches
    match_count = len(matches)
    similar_matches = sum([1 for m in matches if m.distance < threshold * 96])  # Adjust threshold
    similarity_score = similar_matches / match_count

    print(f"Similarity Score: {similarity_score * 100:.2f}")

    return similarity_score > threshold

def classify_image(img_path, model):
    """Load and classify an image using the pre-trained MobileNetV2 model."""
    try:
        # Load the image, resize it to the size expected by MobileNetV2 (224x224), and convert it to an array
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)

        # Preprocess the image (same preprocessing as MobileNetV2 training)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array = preprocess_input(img_array)

        # Predict the class probabilities for the image
        predictions = model.predict(img_array)

        # Decode the top prediction and get the tag (label)
        decoded_predictions = decode_predictions(predictions, top=1)
        tag = decoded_predictions[0][0][1]  # Get the tag (label) of the top prediction

        return tag
    except Exception as e:
        print(f"Error classifying {img_path}: {e}")
        return "Error"

def classify_images_in_folder(model):
    """Classify all images in a folder and save the results in a text file."""
    # Get a list of all image files in the folder (jpg, png, etc.)
    folder_path = f'{os.getcwd()}\\images'
    image_files = glob.glob(os.path.join(folder_path, '*.[jp][pn]g'))  # Matches .jpg, .jpeg, .png
    
    # Loop through each image file in the folder
    for image_file in image_files:
        # Get the image file name without the folder path
        image_filename = os.path.basename(image_file)
        
        # Classify the image and get the tag
        tag = classify_image(image_file, model)
        sql.add_tags_to_image(image_file, image_filename, [tag])
        # print(sql.get_images_for_tag(tag)) ## Debug


if __name__ == "__main__":
    folder_path = f'{os.getcwd()}\\images'
    img1_path = f'{folder_path}\\image (4).jpg'  # Replace with your image path
    img2_path = f'{folder_path}\\image (5).jpg' # Replace with your image path

    if is_image_similar(img1_path, img2_path):
        print("The images are similar.")
    else:
        print("The images are not similar.")