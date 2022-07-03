#! python3
#  readCensusExcel.py - Tabulates population and number of census tracts for
#  each county.

import openpyxl, pprint

output_data = {}

# Open and read the cells of the Excel document with the openpyxl module
print("Opening workbook....")
spreadsheet = openpyxl.load_workbook(
    "chapter_13-read-CensusData-Excel/censuspopdata.xlsx"
)
main_sheet = spreadsheet["Population by Census Tract"]

# Calculate all the tract and population data and store it in a data structure
for row in range(2, main_sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract
    state = main_sheet["B" + str(row)].value
    county = main_sheet["C" + str(row)].value
    population = main_sheet["D" + str(row)].value

    # Make sure the key for this state exists
    output_data.setdefault(state, {})
    # Make sure the key for this county in this state exists
    output_data[state].setdefault(county, {"population": 0, "tracts": 0})

    # Each row represents one census tract, so increment by one
    output_data[state][county]["tracts"] += 1
    # Increase the county population by the population in this census tract
    output_data[state][county]["population"] += int(population)


# Write the data to a file with .py extension using the pprint module
file_name = "census2010.py"
print(f"Writing results to '{file_name}'")
results = open(file_name, "w")
results.write("census_data = " + pprint.pformat(output_data))
results.close()
