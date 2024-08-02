
import os

# Specify the directory to list the contents of
directory_path = os.getcwd()  # You can change this to any path

# Get the list of files and directories in the specified directory
contents = os.listdir(directory_path)

# Print each item in the directory
for item in contents:
    print(item)
