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

# Load the pre-trained MobileNetV2 model
model = applications.MobileNetV2(weights='imagenet')

def classify_image(img_path):
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

def classify_images_in_folder():
    """Classify all images in a folder and save the results in a text file."""
    # Get a list of all image files in the folder (jpg, png, etc.)
    folder_path = f'{os.getcwd()}\\images'
    image_files = glob.glob(os.path.join(folder_path, '*.[jp][pn]g'))  # Matches .jpg, .jpeg, .png
    
    # Loop through each image file in the folder
    for image_file in image_files:
        # Get the image file name without the folder path
        image_filename = os.path.basename(image_file)
        
        # Classify the image and get the tag
        tag = classify_image(image_file)
        sql.add_tags_to_image(image_file, image_filename, [tag])
        # print(sql.get_images_for_tag(tag)) ## Debug

# Main function to run the code
if __name__ == "__main__":
    folder_path = f'{os.getcwd()}\\images'

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        classify_images_in_folder()
        print("Image classification complete.")
    else:
        print("Invalid folder path. Please try again.")
