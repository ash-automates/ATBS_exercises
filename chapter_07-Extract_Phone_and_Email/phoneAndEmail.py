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
# TODO: Create email regex.

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.
