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

    # Find the URL of the comic image
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    comic = soup.select("#comic img")

    # Download the image or indicate the image was not found
    if comic == []:
        print("Could not find comic image.")
    else:
        comic_link = "https:" + comic[0].get("src")
        print(f"Downloading image from '{comic_link}'")
        downloaded = requests.get(comic_link)
        downloaded.raise_for_status()

    # Save the image to the folder
    image_file = open(os.path.join("xkcdComics", os.path.basename(comic_link)), "wb")
    for packet in downloaded.iter_content(100000):
        image_file.write(packet)
    image_file.close()

    # Get the previous button's url before starting the next loop
    prev_link = soup.select("a[rel='prev']")[0]
    url = "https://xkcd.com" + prev_link.get("href")

print("Done!")
