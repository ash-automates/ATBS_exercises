#! python3
# phoneAndEmail.py - Finds phone numbers & email addresses on the clipboard

import pyperclip, re

phoneRegex = re.compile(
    r"""(
    (\d{3}|\(\d{3}\))?  # Area Code
    (\s|-|\.)?          # Separator
    (\d{3})             # First 3 digits
    (\s|-|\.)           # Separator
    ({\d{4}})           # Last 4 digits
    )""",
    re.VERBOSE,
)

emailRegex = re.compile(
    r"""(
    [A-Za-z0-9._%+-]+
    @
    [A-Za-z0-9.-]+
    (\.[A-Za-z]{2,4})
    )""",
    re.VERBOSE,
)
# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.
