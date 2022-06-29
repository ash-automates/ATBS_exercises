#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

# Create folder to store the comics & store the front page URL in a var
url = "https://xkcd.com"
os.makedirs("xkcdComics", exist_ok=True)

while not url.endswith("#"):
    # Download the page
    print(f"Downloading page '{url}'")
    res = requests.get(url)
    res.raise_for_status()

    # TODO: Find the URL of the comic image

    # TODO: Download the image

    # TODO: Save the image to the folder

    # TODO: Get the Prev button's url

print("Done!")
