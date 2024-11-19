---

# Lilac Valley Farm Stay Website

A responsive single-page website for **Lilac Valley Farm Stay**, designed as part of a university project. The website showcases the charm of Lilac Valley Farm Stay, with sections for a hero banner, about information, gallery, bookings, and contact details. The website is fully responsive and meets the specified project requirements.

---

## **Features**

1. **Responsive Design**: Optimized for desktop, tablet, and mobile devices.
2. **Single-Page Scrolling Design**: Smooth navigation through a sticky header.
3. **Dynamic Content**:
   - Hero section images fetched from an AWS S3 bucket.
   - Gallery thumbnails dynamically loaded from an S3 bucket via Flask API.
4. **Booking Form**: Includes fields for user input (e.g., name, email, check-in/out dates) with validation.
5. **Accessibility**:
   - ARIA roles and labels for better usability.
   - Descriptive `alt` attributes for images.
6. **Hosting**: Deployed using AWS EC2, Flask, and Gunicorn.

---

## **Tech Stack**

- **Frontend**: 
  - HTML5, CSS3, JavaScript
- **Backend**:
  - Flask (Python) for serving dynamic content.
- **AWS**:
  - S3: For hosting hero and gallery images.
  - EC2: For hosting the application.
- **Other Tools**:
  - Font Awesome: Icons for contact details.
  - Boto3: AWS SDK for Python to interact with S3.

---

## **Getting Started**

### Prerequisites

1. Python 3.10+
2. Pip and virtual environment tools.
3. AWS CLI configured with proper credentials.
4. Flask and required Python libraries.

### Installation

1. **Clone the Repository**:
   bash
   git clone https://github.com/lil.merce/lilac-valley.git
   cd lilac-valley
   

2. **Set Up a Virtual Environment**:
   bash
   python3 -m venv myenv
   source myenv/bin/activate
   

3. **Install Dependencies**:
   bash
   pip install -r requirements.txt
   

4. **Set AWS Credentials**:
   Ensure your AWS CLI is configured with the credentials that have access to the S3 bucket.
   bash
   aws configure
   

5. **Run the Application**:
   bash
   python app.py
   
   The website will be available at `http://127.0.0.1:8080`.

---

## **Directory Structure**


plaintext
lilac-valley/
├── static/
│   ├── css/
│   │   └── style.css       # Website styling
│   ├── images/             # Static branding assets
│   ├── js/
│   │   └── script.js       # Client-side JavaScript
├── templates/
│   └── index.html          # Main HTML file
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation


---

## **Deployment**

### Set Up AWS EC2

1. Launch an EC2 instance with Ubuntu.
2. Install required dependencies:
   bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip -y
   
3. Clone the repository and set up the virtual environment.

### Run the Flask Application

bash
sudo python3 app.py


### Expose Port 8080

Ensure port 8080 is open in the EC2 security group settings.

### Access the Website

Use the public IP of your EC2 instance, e.g., `http://<ec2-public-ip>:8080`.

---

## **Using Gunicorn for Production**

1. **Install Gunicorn**:
   bash
   pip install gunicorn
   

2. **Test Gunicorn**:
   Run Gunicorn manually to ensure it works with your Flask app:
   bash
   gunicorn -w 4 -b 0.0.0.0:8080 app:app
   
   - `-w 4`: Number of worker processes (adjust based on your instance’s CPU).
   - `-b 0.0.0.0:8080`: Binds the app to port 8080 and allows access from external IPs.

3. **Access the Website**:
   Use your EC2 instance's public IP or DNS, e.g., `http://<ec2-public-ip>:8080`.

---

## **Optional: Running Flask with Gunicorn as a Systemd Service**

To ensure your Flask app starts automatically on boot using Gunicorn:

1. **Create a Systemd Service File**:
   bash
   sudo nano /etc/systemd/system/flaskapp.service
   

2. **Add the Following Configuration**:
   ini
   [Unit]
   Description=A Flask app served with Gunicorn
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/lilac-valley
   Environment="PATH=/home/ubuntu/myenv/bin"
   ExecStart=/home/ubuntu/myenv/bin/gunicorn -w 4 -b 0.0.0.0:8080 app:app

   [Install]
   WantedBy=multi-user.target
   

   - Replace `/home/ubuntu/` with your actual EC2 instance’s directory structure.

3. **Enable and Start the Service**:
   bash
   sudo systemctl enable flaskapp
   sudo systemctl start flaskapp
   

4. **Check Service Status**:
   bash
   sudo systemctl status flaskapp
   

5. **Reload Systemd** (if any changes are made to the service file):
   bash
   sudo systemctl daemon-reload
   

The service will now ensure your Flask app runs in the background, restarts on boot, and listens on port 8080.

---

## **Images and Assets**

- All hero and gallery images are hosted on AWS S3.
- **S3 Bucket Structure**:
  
  plaintext
  lilac-valley-images/
  ├── images/
  │   ├── hero/            # Hero section images
  │   └── gallery/         # Gallery images
  

## **Credits**

- **Author**: Thomas Lambert
- **Purpose**: Built for Curtin University as part of a design and development assignment.

---

## **License**

This website has been created as part of an assignment in an approved course of study for Curtin University and contains copyright material not created by the author. All copyright material used remains copyright of the respective owners.

--- 
