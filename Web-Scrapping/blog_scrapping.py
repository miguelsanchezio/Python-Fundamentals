import requests
from bs4 import BeautifulSoup
from csv import DictWriter

url = "https://www.rithmschool.com/"


def get_next_page(soup):
    page_current = soup.find(class_="current")
    return page_current.find_next_sibling()


def get_soup(url, page_url):
    response = requests.get(url + page_url)
    return BeautifulSoup(response.text, "html.parser")


soup = get_soup(url, "blog")
all_articles = soup.find_all("article")
page_next = get_next_page(soup)

while page_next:
    page_next_url = page_next.contents[1]["href"]
    soup = get_soup(url, page_next_url)

    new_articles = soup.find_all("article")
    all_articles.extend(new_articles)

    page_next = get_next_page(soup)

with open("blog_data.csv", "w") as file:
    headers = ["Title", "URL", "Date"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()

    for article in all_articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag["href"]
        date = article.find("time")["datetime"]

        csv_writer.writerow({
            "Title": title,
            "URL": url,
            "Date": date
        })


