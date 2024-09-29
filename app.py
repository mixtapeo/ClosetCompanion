# Flask app

from flask import Flask, request, jsonify, session, render_template, Blueprint, logging
from flask_cors import CORS
import ImageClassification
import sql

app = Flask(__name__)

# Load environment variables
# load_dotenv()

# Initialize GPT instance
# gpt_instance = GPT(os.getenv('OPENAI_API_KEY'))
CORS(app)
@app.route('/')
def home():
    """
    Home page
    """
    
    return render_template('index.html') # Landing page

@app.route('/upload', methods=['POST'])
def start_program():
    """
    User interface for starting the program.
    """
    print('Starting program...')

@app.route('/api/update', methods=['GET'])
def update():
    """
    Responsible for updating all images' tags in ./images
    """
    print("Updating cache")
    ImageClassification.classify_images_in_folder()
    return jsonify({"message": "Updated"}), 200

@app.route('/compare/', methods=["GET"])
def compare():
    return jsonify({"message": "Comparison done!"})
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)