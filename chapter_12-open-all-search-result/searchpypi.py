#! python3
# searchpypi.py - Opens several search results.

import bs4, requests, webbrowser, sys

# Fetch results webpage for queries given by sys.argv with requests.get
print("Searching.....")
res = requests.get("https://pypi.org/search/?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links with bs4 module
soup = bs4.BeautifulSoup(res.text, "lxml")
links = soup.select(".package-snippet")

# TODO: Open a browser tab for each result with webbrowser module
