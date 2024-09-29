# Flask app

from flask import Flask, request, jsonify, session, render_template, Blueprint, logging
from flask_cors import CORS
import ImageClassification
import sql
from keras import applications
import os
import urllib.request

app = Flask(__name__)

# Load environment variables
# load_dotenv()

# Initialize GPT instance
# gpt_instance = GPT(os.getenv('OPENAI_API_KEY'))
CORS(app)

@app.route('/api/update', methods=['GET'])
def update():
    """
    Responsible for updating all images' tags in ./images
    """
    print("Updating cache")
    
    # Load the pre-trained MobileNetV2 model to be passed into classify_images()
    model = applications.MobileNetV2(weights='imagenet')
    ImageClassification.classify_images_in_folder(model)
    
    return jsonify({"message": "Updated"}), 200

@app.route('/api/compare', methods=["GET", "POST"])
def compare():
    def download_image(url):
        urllib.request.urlretrieve(url, "download.jpg")
    
    if request.method == "POST":
        data = request.get_json()
        link = data.get('link')
        
        if not link:
            return jsonify({"error": "No link provided"}), 400
        
        # Assuming you have a function to download the image from the link
        download_image(link)
        image_incoming = f'{os.getcwd()}\\download.jpg'
        
        for image in os.listdir(f'{os.getcwd()}\\images'):
            image_comparing = f'{os.getcwd()}\\images\\{image}'
            if ImageClassification.is_image_similar(image_comparing, image_incoming):
                return jsonify({"message": 1}) # similar
            else:
                return jsonify({"message": 0}) # different
    else:
        pass
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)