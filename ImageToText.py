import pytesseract
from PIL import Image
import os
import glob

# Optional: Specify the Tesseract command if it's not in your PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_images(folder_path):
    # Get a list of all image files in the folder (jpg, png, etc.)
    image_files = glob.glob(os.path.join(folder_path, '*.[jp][pn]g'))  # Matches .jpg, .jpeg, .png

    # Create or open the output text file in the same folder
    output_file_path = os.path.join(folder_path, 'extracted_texts.txt')
    
    with open(output_file_path, 'w') as output_file:
        # Loop through each image file in the folder
        #pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Fred\AppData\Local\Tesseract-OCR\tesseract.exe'

        for image_file in image_files:
            # Get the image file name without the folder path
            image_filename = os.path.basename(image_file)
            
            try:
                # Open the image
                img = Image.open(image_file)
                print("Image opened", image_filename)

                # Use pytesseract to extract text from the image
                extracted_text = pytesseract.image_to_string(img)

                print("Extracted Text", extracted_text)
                # Write the filename and the extracted text into the output file
                output_file.write(f"File: {image_filename}\n")
                output_file.write("Extracted Text:\n")
                output_file.write(extracted_text + "\n")
                output_file.write("-" * 40 + "\n")  # Add a separator between files

            except Exception as e:
                # Handle errors gracefully
                print(f"Error processing {image_file}: {e}")

# Main function to run the code
if __name__ == "__main__":
    folder_path =  f'{os.getcwd()}\\images'
    
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        extract_text_from_images(folder_path)
        print("Text extraction complete. Check the 'extracted_texts.txt' file in the folder.")
    else:
        print("Invalid folder path. Please try again.")
