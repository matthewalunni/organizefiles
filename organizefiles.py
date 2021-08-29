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
                    print("Moved File: " + fromFile +
                          os.linesep + "To: " + toDestination)
                    pass
                except Exception:
                    pass
            pass
        pass
    pass


def stringContainsKey(dictionary, _str: str):
    """this method checks if a string contains a key of a dictionary

    Args:
        dictionary: dictionary to be checked
        _str: string to be compared with keys

    Returns:
        bool: true if the string contains a key of the dictionary, false otherwise
    """
    for key in dictionary:
        if (key in _str):
            return True

    return False

def getKey(dictionary, string):
    """this method checks if a string contains a key of a dictionary

    Args:
        dictionary: dictionary to be checked
        _str: string to be compared with keys

    Returns:
        string: returns the contained key, none if no key is found
    """
    
    for key in dictionary:
        if (key in string):
            return key

    return ""


if __name__ == "__main__":
    main()
