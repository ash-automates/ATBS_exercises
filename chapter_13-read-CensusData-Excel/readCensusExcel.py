#! python3
#  readCensusExcel.py - Tabulates population and number of census tracts for
#  each county.

import openpyxl, pprint

output_data = {}

# Open and read the cells of an Excel document with the openpyxl module
print("Opening workbook....")
spreadsheet = openpyxl.load_workbook("censuspopdata.xlsx")
main_sheet = spreadsheet["Population by Census Tract"]

# TODO: Calculate all the tract and population data and store it in a data structure

# TODO: Write the data to a file with .py extension using the pprint module
