#!/usr/bin/python3


# pip install --user requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import sys


def crawl(url, depth=0, maxDepth=3, visited=None):
    """
    Given an absolute URL, print each hyperlink found within the document.

    Your task is to make this into a recursive function that follows hyperlinks
    until one of two base cases are reached:

    0) No new, unvisited links are found
    1) The maximum depth of recursion is reached

    You will need to change this function's signature to fulfill this
    assignment.
    """
    if visited is None:
        visited = set()

    if depth > maxDepth:
        return

    try:
        print(" " * 4 * depth + url)
        response = requests.get(url)
        # check if status code of url is >= 400  and therefore likely reachable
        if not response.ok:
            print(f"crawl({url}): {response.status_code} {response.reason}")
            return

        visited.add(url)

        if depth == maxDepth:
            return

        html = BeautifulSoup(response.text, 'html.parser')
        links = html.find_all('a')
        for a in links:
            link = a.get('href')
            if link:
                # Create an absolute address from a (possibly) relative URL
                absoluteURL = urljoin(url, link)
                parsed = urlparse(absoluteURL)
                if parsed.fragment:
                    absoluteURL = absoluteURL.split('#')[0]

                if absoluteURL in visited:
                    continue
                visited.add(absoluteURL)
                if absoluteURL.startswith("http"):
                    crawl(absoluteURL, depth=depth + 1, maxDepth=maxDepth, visited=visited)


    except Exception as e:
        print(f"crawl(): {e}")
    return


## An absolute URL is required to begin
if len(sys.argv) < 2:
    print("Error: no Absolute URL supplied")
    sys.exit(1)
else:
    url = sys.argv[1]

parsed = urlparse(url)
if not parsed.scheme or not parsed.netloc:
    print("The url you provide must be an absolute url")
    sys.exit(1)


if len(sys.argv) > 2:
    maxDepth = sys.argv[2]
    try:
        maxDepth = int(maxDepth)
    except:
        print("Max depth must be an integer")
        sys.exit(1)

    if maxDepth < 0:
        print("Max depth must be an integer greater than zero")
        sys.exit(1)
else:
    maxDepth = 3

plural = 's'
if maxDepth == 1:
    plural = ''

print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")
if len(sys.argv) > 2:
    crawl(url, maxDepth=maxDepth)

else:
    crawl(url)

