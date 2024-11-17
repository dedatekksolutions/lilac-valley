
from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='.')

# API endpoint to list hero images
@app.route('/hero-images')
def list_hero_images():
    hero_dir = './images/hero'
    hero_images = [f'/images/hero/{file}' for file in os.listdir(hero_dir) if file.endswith('.jpg')]
    return jsonify(hero_images)

# Endpoint to list gallery images
@app.route('/gallery-images')
def list_gallery_images():
    gallery_dir = './images/gallery'
    gallery_images = [f'/images/gallery/{file}' for file in os.listdir(gallery_dir) if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.webp')]
    return jsonify(gallery_images)

# Serve the main HTML file
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static files (JavaScript, CSS, images, etc.)
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(port=8080)
