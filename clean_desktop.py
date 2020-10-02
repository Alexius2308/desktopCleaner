from os.path import join, expanduser, exists
import os
import sys
import shutil

def read_file(file_name):
    typo_dict = dict()
    try:
        with open(file_name, encoding="utf-8") as file:
            content=file.readlines()
            for line in content: 
                line = line.split()
                typo_dict[line.pop(0).strip(',')] = line
            return typo_dict
    except FileNotFoundError:
        print("File with type names was not found in script directory!!!",
              "Find your file or just create new.", sep="\n")
        

if __name__ == "__main__":
    types_dict = read_file('custom_types.txt') # Read data with file allocation rules
    home = expanduser("~")
    desktop_path = join(home, "Desktop")
    for key in types_dict.keys(): # Check directories(folders) existence or creation of it
        ooo = join(home, key)
        if exists(ooo):
            print(key, "exists")
        else:
            os.mkdir(join(home, key))
            print("Created '{folder}' folder in user directory".format(folder=key))
    desktop_files = os.listdir()
    for file in desktop_files: # File relocation to specific folders
        if file is not sys.argv[0] and file != 'custom_types.txt': # Check if our script and config in Desktop folder 
            for folder, types in types_dict.items():
                for file_type in types:
                    if file_type in file:
                        pth_file = join(desktop_path, file)
                        dest_folder = join(home, folder)
                        shutil.move(pth_file, dest_folder)
                        print("Moved to " + dest_folder)
    
