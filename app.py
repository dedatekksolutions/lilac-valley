from flask import Flask, jsonify, send_from_directory
import boto3

app = Flask(__name__)

# Configure AWS credentials and S3 bucket name
S3_BUCKET = "lilac-valley-images"
S3_REGION = "us-east-1"
S3_BASE_URL = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com"

# Initialize S3 client
s3_client = boto3.client('s3')

@app.route('/hero-images')
def list_hero_images():
    """API endpoint to list hero images from S3."""
    hero_prefix = "images/hero/"
    hero_images = []

    # List objects in the "images/hero/" directory
    response = s3_client.list_objects_v2(Bucket=S3_BUCKET, Prefix=hero_prefix)
    for obj in response.get('Contents', []):
        if obj['Key'].endswith(('.jpg', '.png', '.webp')):  # Filter image files
            hero_images.append(f"{S3_BASE_URL}/{obj['Key']}")

    return jsonify(hero_images)

@app.route('/gallery-images')
def list_gallery_images():
    """API endpoint to list gallery images from S3."""
    gallery_prefix = "images/gallery/"
    gallery_images = []

    try:
        # Fetch objects from S3
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET, Prefix=gallery_prefix)
        for obj in response.get('Contents', []):
            if obj['Key'].endswith(('.jpg', '.png', '.webp')):  # Filter for images
                gallery_images.append(f"{S3_BASE_URL}/{obj['Key']}")
    except Exception as e:
        # Return error message if something goes wrong
        return jsonify({"error": "Failed to fetch gallery images", "details": str(e)}), 500

    return jsonify(gallery_images)

@app.route('/')
def serve_index():
    """Serve the main HTML file."""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:filename>')
def serve_static_files(filename):
    """Serve other static files (CSS, JS, images, etc.)."""
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    # Run the app on all network interfaces and port 8080
    app.run(host='0.0.0.0', port=8080)
