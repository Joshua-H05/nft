import bs4
import requests

url = "https://yuan-hu.blogspot.com/2022/07/joshuas-first-post.html"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, "html.parser")  # why should there be no parentheses after "content"?
# Content is a data item not a function, so by saying page.content, you're accessing a data item of an instance of a
# class (e.g. self.name)


def print_links():
    # This function prints None a couple of times in between the links. Is it because there are links that have the
    # "a" tag but don't have href attributes? Yes. Although this is valid html, it is not a good idea
    # Anchor tags ("a" tags) should contain hyperlinks, which come in the form of href attributes, so if there is no
    # href attribute, there is no link, meaning there is no real point in having an anchor tag there
    links = [link.get('href') for link in soup.find_all("a") if link.get("href") is not None]
    # the "a" is a tag that stands for hyperlinks
    for link in links:
        print(link)


if __name__ == "__main__":
    print_links()
