#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import sys, webbrowser, pyperclip

# Get address from clipboard or command line argument
if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

# Open the web browser to the Google Maps page for the address
webbrowser.open("https://www.google.com/maps/place/" + address)
