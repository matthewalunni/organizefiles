import os
import time
import json
import shutil

configurations = [
    {
    "directory": "C:\\Users\\matth\\Documents",
    "mappings": {
        "4F00": "C:\\Users\\matth\\Documents\\School\\COSC 4F00\\",
        "3P97": "C:\\Users\\matth\\Documents\\School\\COSC 3P97\\",
        "2P95": "C:\\Users\\matth\\Documents\\School\\COSC 2P95\\",
        "4P14": "C:\\Users\\matth\\Documents\\School\\COSC 4P14\\",
        "3P91": "C:\\Users\\matth\\Documents\\School\\COSC 3P91\\",
        "ENSU 2P02": "C:\\Users\\matth\\Documents\\School\\ENSU 2P02\\",
        "MHD": "C:\\Users\\matth\\Documents\\Projects\\Web Development\\Maidens Hockey Development\\",
        "VET": "C:\\Users\\matth\\Documents\\Projects\\Web Development\\Visual-Edge-Technology\\",
        "86thestigma": "C:\\Users\\matth\\Documents\\Projects\\Web Development\\86thestigma\\",
    }
    },
    {
    "directory": "C:\\Users\\matth\\Downloads",
    "mappings": {
        "4F00": "C:\\Users\\matth\\Documents\\School\\COSC 4F00\\",
        "3P97": "C:\\Users\\matth\\Documents\\School\\COSC 3P97\\",
        "2P95": "C:\\Users\\matth\\Documents\\School\\COSC 2P95\\",
        "4P14": "C:\\Users\\matth\\Documents\\School\\COSC 4P14\\",
        "3P91": "C:\\Users\\matth\\Documents\\School\\COSC 3P91\\",
        "ENSU 2P02": "C:\\Users\\matth\\Documents\\School\\ENSU 2P02\\",
        "MHD": "C:\\Users\\matth\\Documents\\Projects\\Web Development\\Maidens Hockey Development\\",
        "VET": "C:\\Users\\matth\\Documents\\Projects\\Web Development\\Visual-Edge-Technology\\",
        "86thestigma": "C:\\Users\\matth\\Documents\\Projects\\Web Development\\86thestigma\\",
    }
    }
]

           
def main():
    for config in configurations: 
        dir = config["directory"]
        mappings = config["mappings"]
        print(str("Searching: " + dir))
        for filename in os.listdir(dir):
                # for each filename in the directory
                # if the filename contains the mapping key
                if (stringContainsKey(mappings, filename)):
                    _key = getKey(mappings, filename)
                    toDestination = mappings[_key]
                    fromFile = dir + "\\" + filename
                    try:
                        shutil.move(fromFile, toDestination)
                        print("Moved File: " + fromFile + os.linesep + "To: " + toDestination)
                        pass
                    except Exception:
                        pass
                        

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


if __name__ == "__main__":
    main()