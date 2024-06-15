import os
import shutil
from datetime import datetime

# Function to create a directory if it does not exist
def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# Function to organize files by creation month
def organize_by_creation_month(folderName, files):
    for file in files:
        # Get the creation time of the file
        creation_time = datetime.fromtimestamp(os.path.getctime(file))
        # Get the month and year from the creation time
        month_year = creation_time.strftime('%B %Y')
        # Create the month/year directory if it does not exist
        month_year_folder = os.path.join(folderName, month_year)
        createIfNotExist(month_year_folder)
        # Move the file to the month/year directory
        print(f"Moving {file} to {month_year_folder}")  # Debug print statement
        shutil.move(file, os.path.join(month_year_folder, os.path.basename(file)))
    print(f"Files have been organized by creation month in {folderName} successfully")

# List of all files in the current directory, excluding directories
files = [f for f in os.listdir() if os.path.isfile(f)]
files.remove(os.path.basename(__file__))  # Exclude the script file itself

# Creating necessary directory
createIfNotExist('Organized_By_Month')

# Organizing files by creation month
organize_by_creation_month("Organized_By_Month", files)
