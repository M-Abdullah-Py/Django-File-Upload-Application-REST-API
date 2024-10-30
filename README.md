# Django File Upload Application
## Overview
This project is a Django-based application that allows users to upload files, manage them in organized folders, and download them as zip files. It utilizes the Django REST Framework to handle file uploads securely and efficiently, providing a simple interface for users to interact with.

### Key Components:
* File Upload Functionality: Users can upload multiple files at once, which are stored in dynamically created folders.
* Folder Management: Each upload creates a new folder identified by a unique UUID, allowing for organized storage of files.
* Download as Zip: Users can download all files within a folder as a zip archive.
* Frontend Interface: The application features a user-friendly interface built with HTML, CSS, and Bootstrap for responsive design, ensuring a smooth user experience.
### Features
* File Upload: Multiple file uploads are supported through a sleek UI, utilizing the FilePond library for enhanced file management.
* Secure API: Uses Django REST Framework to create a secure backend for file handling.
* Dynamic Folder Creation: Automatically generates folders for each upload, with unique identifiers for easy access.
* File Download: Users can download files in zip format from a dedicated download page.
Technical Details
* Framework: Django REST Framework for building APIs.
* Frontend Libraries: Bootstrap for responsive design and FilePond for file uploads.
* File Management: Uses Django's built-in models to create and manage file storage dynamically.
* User Interaction: JavaScript functions for handling file uploads, copying URLs, and displaying messages.
### Installation
To set up the project, follow these steps:

### Clone the repository:
git clone https://github.com/M-Abdullah-Py/Recipe-and-Student-Report-Card-Project.git

cd Recipe-and-Student-Report-Card-Project
### Install required packages:
pip install -r requirements.txt
### Run migrations:

python manage.py migrate
### Start the development server:

python manage.py runserver
### Usage
* Open your web browser and navigate to http://127.0.0.1:8000/.
* Use the file input to select multiple files for upload.
* Click the "Upload File" button to send your files to the server.
* Upon successful upload, a URL to download the files will be provided, which can be copied with the click of a button.
### Contribution
Contributions are welcome! If you have suggestions for improvements or enhancements, please fork the repository and submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
