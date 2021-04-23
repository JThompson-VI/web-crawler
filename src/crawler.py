#!/usr/bin/python3


# pip install --user requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import sys


def crawl(url):
    """
    Given an absolute URL, print each hyperlink found within the document.

    Your task is to make this into a recursive function that follows hyperlinks
    until one of two base cases are reached:

    0) No new, unvisited links are found
    1) The maximum depth of recursion is reached

    You will need to change this function's signature to fulfill this
    assignment.
    """

    print("\tTODO: Check the current depth of recursion; return now if you have gone too deep")
    try:
        print("\tTODO: Print this URL with indentation indicating the current depth of recursion")
        response = requests.get(url)
        if not response.ok:
            print(f"crawl({url}): {response.status_code} {response.reason}")
            return

        html = BeautifulSoup(response.text, 'html.parser')
        links = html.find_all('a')
        for a in links:
            link = a.get('href')
            if link:
                # Create an absolute address from a (possibly) relative URL
                absoluteURL = urljoin(url, link)

                # Only deal with resources accessible over HTTP or HTTPS
                if absoluteURL.startswith('http'):
                    print(absoluteURL)

        print("\n\tTODO: Don't just print URLs found in this document, visit them!")
        print("\tTODO: Trim fragments ('#' to the end) from URLs")
        print("\tTODO: Use a `set` data structure to keep track of URLs you've already visited")
        print("\tTODO: Call crawl() on unvisited URLs")

    except Exception as e:
        print(f"crawl(): {e}")
    return


## An absolute URL is required to begin
if len(sys.argv) < 2:
    print("Error: no Absolute URL supplied")
    sys.exit(1)
else:
    url = sys.argv[1]

print("\tTODO: determine whether variable `url` contains an absolute URL")

print("\tTODO: allow the user to optionally override the default recursion depth of 3")
maxDepth = 3

plural = 's'
if maxDepth == 1:
    plural = ''

print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")
print("\tTODO: crawl() keeps track of the max depth itself: no globals allowed!")
crawl(url)

print("\tTODO: delete each TODO message as you fulfill it")
