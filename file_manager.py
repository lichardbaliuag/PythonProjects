
import os
import time

# Source Path 
# # 1. Check files in source path
currentPath = os.getcwd()
print(currentPath)

# Check Download folder
download_folder = os.path.expanduser("~")+"/Downloads/"

# Destination Path
    # 2. Create folder according to file type

# Create new folder for file type
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error creating directory:' + directory)

createFolder(currentPath + ' TestFolder_01')

# Move file to specific folder according to file type

### ----------------------- ###

from watchdog.observers import Observer
from .events import ImagesEventHandler

class ImagesWatcher:
    def __init__(self, src_path):
        self.__src_path = src_path
        self.__event_handler = ImagesEventHandler()
        self.__event_observer = Observer()

    def run(self):
        self.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__src_path,
            recursive=True
        )

if __name__ == "__main__":
    src_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    ImagesWatcher(src_path).run()