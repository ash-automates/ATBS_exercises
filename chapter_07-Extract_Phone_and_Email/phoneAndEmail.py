#! python3
# phoneAndEmail.py - Finds phone numbers & email addresses on the clipboard

import pyperclip, re

phoneRegex = re.compile(
    r"""(
    (\d{3}|\(\d{3}\))?  # Area Code
    (\s|-|\.)?          # Separator
    (\d{3})             # First 3 digits
    (\s|-|\.)           # Separator
    (\d{4})           # Last 4 digits
    )""",
    re.VERBOSE,
)

emailRegex = re.compile(
    r"""(
    [A-Za-z0-9._%+-]+   # Username
    @                   # @ symbol
    [A-Za-z0-9.-]+      # Domain name
    (\.[A-Za-z]{2,4})   # Dot "something"
    )""",
    re.VERBOSE,
)

# Find matches in the clipboard text.
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

print(matches)
# TODO: Copy results to the clipboard.
