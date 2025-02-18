import os
import json

PDF_FOLDER = "pdfs"
OUTPUT_FILE = "books.json"

def update_books():
    books = [f.replace(".pdf", "") for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]
    
    with open(OUTPUT_FILE, "w") as f:
        json.dump(books, f, indent=4)

if __name__ == "__main__":
    update_books()
    print("Updated books.json with current PDFs.")
