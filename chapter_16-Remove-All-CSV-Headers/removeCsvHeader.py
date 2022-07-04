#! python3
#  removeCsvHeader.py - Removes the header from all CSV files in the current
#  working directory.

import csv, os

# Create a folder for the headless CSV files to be stored in
os.makedirs("headless CSVs", exist_ok=True)

# Loop through every file in the current working directory & skip non-CSV files
for file_name in os.listdir("."):
    if not file_name.endswith(".csv"):
        continue

    # TODO: Read each CSV file into memory while skipping its first row

    # TODO: Write out the headless CSV file & save it into the folder
