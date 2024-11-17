from flask import Flask, jsonify, send_from_directory
import boto3
import os

# Initialize Flask app
app = Flask(__name__, static_folder='.')

# S3 bucket details
S3_BUCKET_NAME = 'lilac-valley-images'
S3_BUCKET_URL = f'https://{S3_BUCKET_NAME}.us-east-1.amazonaws.com.com'

# Initialize the S3 client
s3_client = boto3.client('s3')

def list_s3_images(prefix):
    """
    List all image files in the specified S3 directory (prefix).
    Args:
        prefix (str): Directory prefix in the S3 bucket (e.g., 'images/hero/')
    Returns:
        list: List of full URLs to the images.
    """
    try:
        # List objects in the specified prefix (directory) of the S3 bucket
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET_NAME, Prefix=prefix)

        # Check if any files exist in the directory
        if 'Contents' not in response:
            print(f"No files found in S3 directory: {prefix}")
            return []

        # Generate URLs for image files with supported extensions
        return [
            f'{S3_BUCKET_URL}/{item["Key"]}'
            for item in response['Contents']
            if item['Key'].lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))
        ]
    except Exception as e:
        print(f"Error listing objects in S3: {e}")
        return []

# API endpoint to list hero images dynamically
@app.route('/hero-images')
def list_hero_images():
    hero_images = list_s3_images('images/hero/')
    if not hero_images:
        return jsonify({"error": "No hero images found"}), 404
    return jsonify(hero_images)

# API endpoint to list gallery images dynamically
@app.route('/gallery-images')
def list_gallery_images():
    gallery_images = list_s3_images('images/gallery/')
    if not gallery_images:
        return jsonify({"error": "No gallery images found"}), 404
    return jsonify(gallery_images)

# Serve the main HTML file
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static files (JavaScript, CSS, etc.)
@app.route('/<path:path>')
def serve_static_files(path):
    try:
        return send_from_directory(app.static_folder, path)
    except Exception as e:
        print(f"Error serving static file: {e}")
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    # Run the Flask app on port 8000
    app.run(port=8000)
