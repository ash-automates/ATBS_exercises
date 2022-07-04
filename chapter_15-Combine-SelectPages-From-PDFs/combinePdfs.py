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

# Loop through all the PDF files
for pdf_file in pdf_files:
    file_object = open(pdf_file, "rb")
    pdf_reader = PyPDF2.PdfFileReader(file_object)

    # Loop through all the pages (except the first) and add them
    for page_num in range(1, pdf_reader.numPages):
        page_to_add = pdf_reader.getPage(page_num)
        output.addPage(page_to_add)

# TODO: Save the resulting PDF to a file
