#! python3
#  removeCsvHeader.py - Removes the header from all CSV files in the current
#  working directory.

import csv, os

# Create a folder for the headless CSV files to be stored in
os.makedirs("headless_csv_files", exist_ok=True)

# Loop through every file in the current working directory & skip non-CSV files
for file_name in os.listdir("."):
    if not file_name.endswith(".csv"):
        continue

    # Read each CSV file into memory while skipping its first row
    copied_rows = []
    csv_file_object = open(file_name)
    reader_object = csv.reader(csv_file_object)
    for row in reader_object:
        if reader_object.line_num == 1:
            continue
        copied_rows.append(row)
    csv_file_object.close()

    # TODO: Write out the headless CSV file & save it into the folder
