import os
import json
import requests
from pdf2image import convert_from_path

# Set Poppler path directly (update this to match your Poppler path)
os.environ["POPPLER_PATH"] = r"C:\Users\harsh\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin"

PDF_FOLDER = "pdfs"
OUTPUT_FILE = "books.json"

# Function to download PDF from GitHub
def download_pdf_from_github(github_url, download_path):
    """Downloads a PDF file from GitHub and saves it locally."""
    try:
        response = requests.get(github_url)
        if response.status_code == 200:
            with open(download_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {download_path}")
            return True
        else:
            print(f"Failed to download {github_url}. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error downloading PDF from GitHub: {e}")
        return False

def generate_cover(pdf_path, cover_path):
    """Extracts the first page of a PDF and saves it as a JPG cover."""
    try:
        images = convert_from_path(pdf_path, first_page=1, last_page=1)
        images[0].save(cover_path, "JPEG")
        return True
    except Exception as e:
        print(f"Error generating cover for {pdf_path}: {e}")
        return False

def update_books():
    books = []
    
    for file in os.listdir(PDF_FOLDER):
        if file.endswith(".pdf"):
            book_name = file.replace(".pdf", "")
            pdf_path = os.path.join(PDF_FOLDER, file)
            cover_path = os.path.join(PDF_FOLDER, book_name + ".jpg")
            
            # Download PDF from GitHub if not already in the folder
            github_url = f"https://raw.githubusercontent.com/StableMann46/DigitalBooks/main/pdfs/{file}"
            if not os.path.exists(pdf_path):
                if not download_pdf_from_github(github_url, pdf_path):
                    continue

            # Generate cover if it doesn't exist
            if not os.path.exists(cover_path):
                if not generate_cover(pdf_path, cover_path):
                    print(f"Failed to generate cover for {file}")
                    continue

            books.append({"name": book_name, "file": f"./pdfs/{file}", "cover": f"./pdfs/{book_name}.jpg"})

    with open(OUTPUT_FILE, "w") as f:
        json.dump(books, f, indent=4)

if __name__ == "__main__":
    update_books()
    print("Updated books.json and generated covers.")
