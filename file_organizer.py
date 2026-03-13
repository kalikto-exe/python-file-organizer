"""
File Organizer
Created by Kalikto (a.k.a. Smit Mehta)

Organizes files in a folder into categories
like Images, Documents, Videos, and Music.
"""

import os
import shutil

file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"]
}

folder_path = input("Enter folder path to organize: ")

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()
        moved = False

        for folder, extensions in file_types.items():
            if extension in extensions:
                target = os.path.join(folder_path, folder)

                if not os.path.exists(target):
                    os.makedirs(target)

                shutil.move(file_path, os.path.join(target, filename))
                moved = True
                break

        if not moved:
            other = os.path.join(folder_path, "Others")

            if not os.path.exists(other):
                os.makedirs(other)

            shutil.move(file_path, os.path.join(other, filename))

print("Files organized successfully!")
