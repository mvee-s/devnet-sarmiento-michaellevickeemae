"""
Module 2 — Activity: File Sorting with os and shutil
Student: Michaelle Vickeemae G. Sarmiento
Date: September 27, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]


The goal of the script is to ask the user for a folder path 
and eventually organize the files inside that folder into 
different categories such as Images, Documents, Videos, and Others.

However, my script is still unfinished. So far, it asks the 
user to enter a folder path and checks if the folder exists. 
I also created a list of categories for the folders where the 
files will eventually be organized. I was planning to sort the 
files based on their file extensions, but I was not able to complete 
that part during the lab activity. I know how it works, but with coding, 
I am still having a hard time analyzing and implementing.




============================================
KEY VOCABULARY
============================================
- os module: allows interaction with the OS, such as checking files, folders, and path
- shutil module: allows moving or copying files
- file path: the location of the path in the computer
- directory: another term where files and other folders are stored
- os.listdir(): gets the names of files and folders inside a directory
- os.path.exists(): checks if a specified file or folder exists
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""
''''''
import os
import shutil

# --- paste your existing code here ---

# This is my unfinished PROJECT-FO last time in lab. no changes were made after that activity.
import os
import shutil

user_folder = input("Enter the folder path to organize: ")
list_files = [os.listdir()]
list_subfolders = ["Images", "Documents", "Videos", "Others"]
images = 0
documents = 0
videos = 0
others = 0 


if os.path.exists(user_folder):

    for subfolder in list_subfolders:
        if os.path.exists(subfolder):
            print(subfolder)

    
        

    
else:
    print("The folder does not exist.")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]

One thing I noticed while working on this was that I was able to 
check if the folder exists, but I was not yet properly using the 
folder path when getting the files. I also created the list of 
subfolders, but my code only checks if those folders already exist 
instead of creating them or moving files into them. This made me 
realize that I still needed to connect each part of the code together 
for the file organizer to actually work.

Since this was an unfinished activity, he main thing I want 
to avoid next time is writing different parts of the code without 
checking how they work together. This activity made me realize that 
analyzing first the flow is much helpful that jumping to different 
parts and working on the other part while doing the other. 

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
