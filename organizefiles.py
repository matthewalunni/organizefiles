import os
import time
import shutil
from watchdog.events import FileSystemEventHandler, PatternMatchingEventHandler
from watchdog.observers import Observer 

# the directory to be watched
directory = "C:\\Users\\matth\\Documents"

# these are the mappings for the program
# if a file contains the key, then it is moved to the corresponding value
mappings = {
    "4F00": "C:\\Users\\matth\\Documents\\School\\COSC 4F00\\",
    "3P97": "C:\\Users\\matth\\Documents\\School\\COSC 3P97\\",
    "2P95": "C:\\Users\\matth\\Documents\\School\\COSC 2P95\\"
}

# this class handles what happens when a file is modified in a directory
class OrganizationHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(directory):
            if (stringContainsKey(mappings, filename)):
                _key = getKey(mappings, filename)
                toDestination = mappings[_key]
                fromFile = directory + "\\" + filename
                shutil.move(fromFile, toDestination)

                        
# this method checks if a string contains a key of a dictionary
# @param dictionary     dictionary to be checked
# @param _str           string to be compared with keys            
def stringContainsKey(dictionary, _str):
    for key in dictionary:
        if (key in _str):
            return True
    
    return False

# this method checks if a string contains a key of a dictionary
# @param dictionary     dictionary to be checked
# @param _str           string to be compared with keys   
# @return               returns the contained key
def getKey(dictionary, string):
    for key in dictionary:
        if (key in string):
            return key
    
    return ""

event_handler = OrganizationHandler()
observer = Observer()
observer.schedule(event_handler, directory, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()