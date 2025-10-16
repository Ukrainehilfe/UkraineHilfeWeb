
import zipfile
import os
from datetime import datetime

def create_project_zip():
    # Create a timestamp for the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = f"ukraine-hilfe-osnabrueck_{timestamp}.zip"
    
    # Files to include in the ZIP
    files_to_zip = [
        'index.html',
        'style.css',
        'script.js',
        '.replit'
    ]
    
    # Create the ZIP file
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add main files
        for file in files_to_zip:
            if os.path.exists(file):
                zipf.write(file)
        
        # Add assets folder if it exists
        if os.path.exists('assets'):
            for root, dirs, files in os.walk('assets'):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path)
        
        # Add config folder if it exists
        if os.path.exists('.config'):
            for root, dirs, files in os.walk('.config'):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path)
    
    print(f"✅ Project packaged successfully as: {zip_filename}")
    print(f"📦 ZIP file contains all your website files")
    print(f"📁 You can download this file from the Files panel")
    
    return zip_filename

if __name__ == "__main__":
    create_project_zip()
