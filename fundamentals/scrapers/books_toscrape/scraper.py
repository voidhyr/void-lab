import time
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup

from fundamentals.scrapers.books_toscrape.db import init_db, save_book, fetch_summary

current_url = "https://books.toscrape.com/"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
}

all_books = []
page_count = 0

rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def clean_price(price_str: str):
    cleaned_value = price_str.replace("£", "").strip()
    return float(cleaned_value)


def parse_rating(rating_word: str) -> int:
    return rating_map.get(rating_word, 0)


init_db()
while current_url:
    response = httpx.get(current_url, headers=header)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(response.status_code)

    books = soup.find_all("article", class_="product_pod")
    # print(len(books))
    for book in books:
        h3_tag = book.find("h3")
        if h3_tag:
            a_tag = h3_tag.find("a")
            title = a_tag["title"]
            link = a_tag["href"]
            full_link = urljoin(current_url, link)
            # print(title)
            # print(link)

        price_tag = book.find("p", class_="price_color")
        price = clean_price(price_tag.text) if price_tag else 0.0
        # print(type(price))

        rating_tag = book.find("p", class_="star-rating")
        rating_classes = rating_tag.get("class", []) if rating_tag else []
        rating_word = rating_classes[1] if len(rating_classes) > 1 else ""
        rating_num = parse_rating(rating_word)
        
        stock_tag = book.find("p", class_="instock availability")
        stock_status = stock_tag.text
        stock_status = stock_status.strip()

        # print(rating_word)
        # print(stock_status)
        rating_word = rating_word[1]
        rating_num = rating_map.get(rating_word, 0)
        # print(rating_num)

        book_dict = {"title": title, "link": full_link, "price": price,
                     "rating": rating_num, "stock": stock_status}
        all_books.append(book_dict)

    next_li = soup.find("li", class_="next")
    if next_li:
        next_a = next_li.find("a")
        if next_a:
            next_href = next_a["href"]
            current_url = urljoin(current_url, next_href)
    else:
        current_url = None

    page_count += 1
    time.sleep(1)
    if page_count == 2:
        break

print(len(all_books))
save_book(all_books)
count, avg_price = fetch_summary()
print(f"Stored {count} books in database. Average price: £{avg_price:.2f}")
