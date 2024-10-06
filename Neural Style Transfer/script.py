from flask import Flask, render_template, request, jsonify
import base64
from PIL import Image
import io
import numpy as np
import os

app = Flask(__name__)

# Dummy function for image processing (Replace with your actual model logic)
def generate_image(content_image):
    # Simulate image processing (Neural Style Transfer or cGAN)
    # For now, we'll just convert the image to grayscale as a placeholder
    image = Image.open(content_image)
    image = image.convert('L')  # Convert to grayscale (just a placeholder)
    
    # Convert the processed image back to a format we can send as a response
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image_endpoint():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    content_image = request.files['file']
    
    if content_image.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    # Run the style transfer or image-to-image translation
    image_data = generate_image(content_image)
    
    return jsonify({"image_data": image_data})

if __name__ == '__main__':
    app.run(debug=True)
