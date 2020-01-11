import os
import json
import time
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        #new_name = "new_file_" + str(self.i) + ".txt"
        for filename in os.listdir(folder_to_track):
            file_exists = os.path.isfile(folder_destination + "/" + new_name)
            while file_exists:
                self.i += 1
                new_name = "new_file_" + str(self.i) + ".txt"

            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filenamep
            os.rename(src, new_destination)
            
    folder_to_track = "/Users/lichardbaliuag/Desktop/TestFolder_01"
    folder_destination = "/Users/lichardbaliuag/Desktop/TestFolder_02"
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def on_created(event):
    print("hey, {event.src_path} has been created!")

def on_deleted(event):
    print("Someone deleted a file in {event.src_path}")

def on_modified(event):
    print("Someone modified a file in {event.src_path}")

def on_moved(event):
    print("Someone moved {event.src_path} to {event.dest_path}")

my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved

path = "/Users/lichardbaliuag/Desktop/TestFolder_01"        # "."
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()

# if __name__ == "__main__":
#     patterns = "*"
#     ignore_patterns = ""
#     ignore_directories = False
#     case_sensitive = True
#     my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)



