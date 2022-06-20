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

    # Create the ZIP file
    print(f"Creating {zip_name}.....")
    back_up = zipfile.ZipFile(zip_name, "w")

    # Walk the entire folder tree and compress the files in each folder
    for currentFolder, subFolders, filenames in os.walk(folder):
        print(f"Adding files in {currentFolder}")
        back_up.write(currentFolder)
        for filename in filenames:
            newBase = os.path.basename(filename) + "_"
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue
            back_up.write(os.path.join(currentFolder, filename))

    # Close the backup file when done
    back_up.close()
    print("Done!")
