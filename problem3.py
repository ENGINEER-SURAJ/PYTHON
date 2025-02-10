import os

# Specify the directory path
directory_path = "C:\PHOTOS 2"  # Replace with your desired path

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
  print(item)
