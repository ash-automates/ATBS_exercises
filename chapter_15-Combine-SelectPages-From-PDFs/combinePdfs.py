#! python3
#  combinePdfs.py - Combines all the PDFs in the current working directory into
#  into a single PDF.

import PyPDF2, os

# Get all the PDF filenames from the current directory
pdf_files = []

for file_name in os.listdir("."):
    if file_name.endswith(".pdf"):
        pdf_files.append(file_name)

# Sort the filenames so the PDFs are added in order
pdf_files.sort(key=str.lower)

# Create a PdfFileWriter object for the output PDF
output = PyPDF2.PdfFileWriter()

# TODO: Loop through all the PDF files

# TODO: Loop through all the pages (except the first) and add them

# TODO: Save the resulting PDF to a file
