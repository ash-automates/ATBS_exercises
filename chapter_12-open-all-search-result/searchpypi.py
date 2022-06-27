#! python3
# searchpypi.py - Opens several search results.

import bs4, requests, webbrowser, sys

# Fetch results webpage for queries given by sys.argv with requests.get
print("Searching.....")
res = requests.get(
    "https://google.com/search?q="
    + "https://pypi.org/search/?q="
    + " ".join(sys.argv[1:])
)
res.raise_for_status()

# TODO: Retrieve top search result links with bs4 module

# TODO: Open a browser tab for each result with webbrowser module
