import requests
from bs4 import BeautifulSoup
from csv import DictWriter


def get_soup(base_url, page_url=""):
    response = requests.get(base_url + page_url)
    return BeautifulSoup(response.text, "html.parser")


url = "http://quotes.toscrape.com"
quotes = []

soup = get_soup(url)
page_quotes = soup.find_all(class_="quote")

while len(page_quotes) > 0:
    for q in page_quotes:
        quote = q.contents[1].get_text()
        author = q.contents[3].contents[1].get_text()
        author_url = q.contents[3].contents[3]["href"]
        quotes.append({
            "Quote": quote,
            "Author": author,
            "Author URL": author_url
        })

    next_page = soup.find(class_="next")

    if next_page:
        next_page_url = next_page.contents[1]["href"]
        soup = get_soup(url, next_page_url)
        page_quotes = soup.find_all(class_="quote")
    else:
        break

with open("quotes.csv", "w") as file:
    csv_writer = DictWriter(file, fieldnames=["Quote", "Author", "Author URL"])
    csv_writer.writeheader()
    for quote in quotes:
        csv_writer.writerow(quote)
