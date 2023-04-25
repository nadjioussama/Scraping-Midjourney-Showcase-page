A script to scrape the content of the showcase page of midjourney website : https://www.midjourney.com/showcase/

The file download.json is retrieved from their api : https://www.midjourney.com/api/public-feed/?orderBy=top

You can replace "orderBy=top" by "orderBy=hot"

Sometimes you need to clean the json from some random special characters in "promp" because it's used in naming the files like (\" , < , ° ...)


EDIT:

The old Internal API doenst work, so the link https://www.midjourney.com/api/public-feed/?orderBy=top doesnt give you anything.

I added Midjourney2.py that uses Selenium just to fetch image links, then the download is done is requests.

Enjpy.
