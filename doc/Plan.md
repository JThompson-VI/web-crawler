*Replace the bold text with your own content*

*Adapted from https://htdp.org/2020-5-6/Book/part_preface.html*

# 0.  From Problem Analysis to Data Definitions

    -what the system is currently doing
        - sends get request for provided absolute URL
        - ensures the status code is < 400
        - parses the contents of the html document for <a> tags and extracts the links from them as strings
            - creates an absolute URL from possible partial URL given by href
        - prints all links on the page with scheme http or https

    - what it needs to do that it isn't already doing
        - crawl must take parameters: URL, depth, maxDepth, visited
            - maxDepth default value is three or is argv[2] if supplied by user
            - visited is a set of already visited URL's
            - depth starts at 0
        - crawl must include the base case if no new links are found return out of crawl
        - base case 2: if depth = maxDepth visit and print all unvisited links
        - if depth < maxDepth call crawl recursively with the url of the first encountered link.
            - increment depth
            - update visited
            - print visited url with tabs indicating depth
        - use urlparse to discard any fragments, treat url with fragment as same as url without


# 1.  System Analysis
*Signature*
def crawl(URL, depth=0, maxDepth=3, visited=set())
parameters
-------------------
- URL is provided from the command line and is required
    - function will not handle error for when url is not provided
- depth will always start at 0
- maxDepth can be provided by the user from the command line (must be a positive integer CAN BE 0)
    - Remember to convert sys.argv[2] into an int
    - function will not check for input validity
- visited is always an empty set
--------------------------
data flow through function
--------------------------
- Check current depth of recursion return immediately if depth > maxDepth
- print url with spaces * 4 * depth (to indicate depth of recursion in output)
- send get request for param URL
    - check status code of response object if not response.ok print status code and reason then return
- parse document provided by param URL
- extract all <a> tags into a list
- iterate over list extracting links via BeautifulSoup(response.text, 'href')
    - if there is a non empty href use urljoin to create an absolute url from possible relative url
    - use urlparse to find fragments
    - if parsed.fragment: split at the hash mark and point new URL at parsed[0]
    - check if the new absolute URL is in visited
        - if in visited continue
        - if not in visited add to visited
            - if depth = maxDepth continue looping through all links and return from crawl
            - check current depth if maxDepth not yet reached
            - leave the loop

            - make a recursive call to crawl with the new URL and increment depth

- crawl returns nothing, all output is in the form of printed statements


# 2.  Functional Examples

def crawl(URL, depth=0, maxDepth=3, visited=set())
    if depth > maxDepth:
        return
    print(" " * 4 * depth + URL)
    response = requests.get(URL)
    if not response.ok:
        print status code and reason info
        return

    if depth = maxDepth:
        return

    html = BeautifulSoup(response.text, 'html.parser')
    links = html.find_all('a')
    for a in links:
        link = a.get('href')
        if link:
            absoluteurl = create absolute url from url and link
            parse absolute url
            if parsed.fragment:
                absoluteurl = absoluteurl.split("#")[0]

            if absoluteurl in visited:
                continue
            add absoluteurl to visited

            if not absoluteurl startswith http:
                continue

            call crawl recursively with (absoluteurl, depth + 1, visited = visited)


# 3.  Function Template

def crawl(url, depth=0, maxDepth=3, visited=set())
    if depth > maxDepth:
        return
    try:
        print(" " * 4 * depth + url)
        response = requests.get(url)
        if not response.ok:
            print(f"crawl({url}): {response.status_code} {response.reason}")
            return

        if depth = maxDepth:
            return

        html = BeautifulSoup(response.text, 'html.parser')
        links = html.find_all('a')
            for a in links:
                link = a.get('href')
                if link:
                    absoluteURL = urljoin(url, link)
                    parsed = urlparse(absoluteURL)
                    if parsed.fragment:
                        absoluteURL = absoluteURL.split('#')[0]
                    if absoluteURL in visited:
                        continue
                    visited.add(absoluteURL)
                    if absoluteURL.startswith('http'):
                        crawl(absoluteURL, depth = depth + 1, maxDepth, visited)




# 4.  Implementation

**This is the only part of the process focused on writing code in your chosen
programming language.**

**One by one translate passages of pseudocode into valid code.  Fill in the gaps
in the function template.  Exploit the purpose statement and the examples.**

**If you were thorough in the previous steps and are familiar with your
programming system this part will go by very quickly and the code will write
itself.**

**When you are learning a new programming language or an unfamiliar library this
phase can be slow and difficult.  As you gain experience with the relevant
technologies you will spend less and less time in this phase of the process.**


# 5.  Testing

**Articulate the examples given in step #2 as tests and ensure that each
function passes all of its tests.  Doing so discovers mistakes.  Tests also
supplement examples in that they help others read and understand the definition
when the need arises—and it will arise for any serious program.**

**As bugs are discovered and fixed, devise new test cases that will detect these
problems should they return.**

**If you didn't come across any bugs (lucky you!) think of a possible flaw and a
test that can be employed to screen for it.**

**At a minimum you should create a document explaining step-by-step how a
non-technical user may manually test your program to satisfy themselves that it
operates correctly.  Explain the entire process starting how to launch the
program, what inputs they should give and what results they should see at every
step.  Provide test cases of good and bad inputs to catch both false positives
and false negatives.  Any deviation from the expected outputs are errors.**

**The ideal is to write an automated test to avoid all manual labor beyond
launching the test.**
