from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import update_books  # Import the update function

class BookWatcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".pdf"):
            update_books.update_books()
            print("PDF folder updated, books.json refreshed.")

if __name__ == "__main__":
    path = "pdfs"
    event_handler = BookWatcher()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
