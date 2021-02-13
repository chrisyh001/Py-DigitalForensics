from __future__ import print_function
import argparse
import os

# create a title for code 
_title_ = "Directory Tree"

# add parser argumants
parser = argparse.ArgumentParser(
    description=_title_,
)
parser.add_argument("DIR_PATH", help="Path to directory")
args = parser.parse_args()
path_to_scan = args.DIR_PATH

# using os.walk in the standard python library 
# create a for loop to 
# iterate over the path_to_scan
for root, directories, files in os.walk(path_to_scan):


# create a for loop to 
# terate over the files in the current "root"
    for file_entry in files:
        # create the relative path to the file
        file_path = os.path.join(root, file_entry)
        # print 
        print(file_path)
        
## Special Thanks to Python Digital Forensics Cookbook By Preston Miller, Chapin Bryce for the code idea ##
