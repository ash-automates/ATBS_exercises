#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.

import pyperclip, sys, shelve

mcb_shelf = shelve.open("mcb")

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords or load content depending on the command line args.
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
