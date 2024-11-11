import os
import shutil

def organize_files(directory):
    # Change to the target directory
    os.chdir(directory)

    # Iterate through all files in the directory
    for filename in os.listdir('.'):
        if os.path.isfile(filename):  # Check if it's a file
            # Get the file extension
            file_extension = filename.split('.')[-1] if '.' in filename else 'no_extension'
            # Create a new directory for the file extension if it doesn't exist
            if not os.path.exists(file_extension):
                os.makedirs(file_extension)
            # Move the file into the corresponding directory
            shutil.move(filename, os.path.join(file_extension, filename))
            print(f'Moved: {filename} to {file_extension}/')

if __name__ == "__main__":
    # Specify the directory to organize
    target_directory = input("Enter the directory path to organize files: ")
    organize_files(target_directory)
