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
    gallery_prefix = "images/gallery/"
    gallery_images = []

    try:
        # Fetch objects from S3
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET, Prefix=gallery_prefix)
        print("S3 Response:", response)  # Debugging

        # Check if the Contents key exists
        if 'Contents' in response:
            for obj in response['Contents']:
                if obj['Key'].endswith(('.jpg', '.png', '.webp')):  # Filter for images
                    gallery_images.append(f"{S3_BASE_URL}/{obj['Key']}")
        else:
            print("No images found in the specified directory.")

    except Exception as e:
        # Print the error for debugging
        print("Error while accessing S3:", str(e))
        return jsonify({"error": "Failed to fetch gallery images", "details": str(e)}), 500

    return jsonify(gallery_images)


# Serve the main HTML file
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve other static files (CSS, JS, images, etc.)
@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory(app.static_folder, filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
