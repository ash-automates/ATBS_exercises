#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os


def backupToZip(folder):
    folder_path = os.path.abspath(folder)  # Make sure folder path is absolute

    # Figure out the new back up file number based on previous backups
    count = 1
    while True:
        zip_name = os.path.basename(folder) + "_" + str(count) + ".zip"
        if not os.path.exists(name_to_check):
            break
        count += 1

    # Create the ZIP file.
    print(f"Creating {zip_name}.....")
    back_up = zipfile.ZipFile(zip_name, "w")
    # TODO: Walk the entire folder tree and compress the files in each folder.
