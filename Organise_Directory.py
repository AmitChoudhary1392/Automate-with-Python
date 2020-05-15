import os
from pathlib import Path

Subdirectories={
    "Documents":['.pdf',".txt",".rtf",".doc"],
    "Images":[".jpg",".jpeg",".png"],
    "Audio":[".m4a",".mp3", ".m4b"],
    "Video":[".mp4",".mov",".avi"]
}                                               # add more sub directories/ folders based on requirements

#function to identify the correct directory
def pickDirectory(value):
    
    for category, suffixes in Subdirectories.items():       #scan through all the items in subdirectories
        for suffix in suffixes:            
            if suffix== value:      #check each suffix for file type
                return category


def OrganiseDirectory():
    
    for item in os.scandir():          #scan items in given directory
        file_path=Path(item)           #path for the file in directory
        file_type= file_path.suffix.lower()     # suffix gives the extension of the file
        directory= pickDirectory(file_type)      # using pickDirectory function to choose output directory
        directory_path= Path(directory)           # identify the path of the directory

        file_path.rename(directory_path.joinpath(file_path))        #change path of file to move it into the respective directory

OrganiseDirectory()