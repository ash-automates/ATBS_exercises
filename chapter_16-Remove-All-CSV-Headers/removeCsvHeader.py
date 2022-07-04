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

    # Write out the headless CSV file & save it into the folder
    overwritten_csv_object = open(os.path.join("headless_csv_files", file_name), "w")
    csv_write_object = csv.writer(overwritten_csv_object)
    for copied_row in copied_rows:
        csv_write_object.writerow(copied_row)
    overwritten_csv_object.close()
