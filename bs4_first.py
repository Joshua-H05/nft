import bs4
import requests
import pysnooper

url = "https://yuan-hu.blogspot.com/2022/07/joshuas-first-post.html"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, "html.parser")  # why should there be no parentheses after "content"?


def print_links():
    links = soup.find_all("a")  # The a stands for "anchor"
    for link in links:
        link = link.get("href")
        if link:
            print(link)

    # This function prints None a couple of times in between the links. Is it because there are links that have the
    # "a" tag but don't have href attributes? For example, "Yu'an Hu" contains a link but the link isn't displayed
    """links = [link.get('href') for link in soup.find_all("a")]  # the "a" is a tag that stands for hyperlinks
    for link in links:
        print(link)"""


if __name__ == "__main__":
    print_links()
