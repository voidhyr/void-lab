import time
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup

from fundamentals.scrapers.books_toscrape.db import (
    fetch_summary,
    init_db,
    save_book,
)

rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def clean_price(price_str: str) -> float:
    cleaned_value = price_str.replace("£", "").strip()
    return float(cleaned_value)


def parse_rating(rating_word: str) -> int:
    return rating_map.get(rating_word, 0)


def parse_page(html: str, base_url: str) -> tuple[list[dict], str | None]:
    soup = BeautifulSoup(html, "html.parser")
    page_books = []

    books = soup.find_all("article", class_="product_pod")
    for book in books:
        h3_tag = book.find("h3")
        title = ""
        full_link = ""
        if h3_tag:
            a_tag = h3_tag.find("a")
            if a_tag:
                title = str(a_tag.get("title", ""))
                link_attr = a_tag.get("href", "")
                full_link = urljoin(base_url, str(link_attr))

        price_tag = book.find("p", class_="price_color")
        price = clean_price(price_tag.text) if price_tag else 0.0

        rating_tag = book.find("p", class_="star-rating")
        raw_classes = rating_tag.get("class") if rating_tag else None
        rating_classes = raw_classes if isinstance(raw_classes, list) else []
        rating_word = str(rating_classes[1]) if len(rating_classes) > 1 else ""
        rating_num = parse_rating(rating_word)

        stock_tag = book.find("p", class_="instock availability")
        stock_status = stock_tag.text.strip() if stock_tag else ""

        # Validate mandatory fields before collecting the record
        if title and full_link:
            book_dict = {
                "title": title,
                "link": full_link,
                "price": price,
                "rating": rating_num,
                "stock": stock_status,
            }
            page_books.append(book_dict)

    next_li = soup.find("li", class_="next")
    if next_li:
        next_a = next_li.find("a")
        if next_a and next_a.get("href"):
            next_url = urljoin(base_url, str(next_a["href"]))
        else:
            next_url = None
    else:
        next_url = None

    return page_books, next_url


def main(max_pages: int = 2) -> None:
    current_url = "https://books.toscrape.com/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) "
            "Gecko/20100101 Firefox/119.0"
        ),
    }
    all_books = []
    page_count = 0

    init_db()

    with httpx.Client(headers=headers, timeout=10.0) as client:
        while current_url and page_count < max_pages:
            try:
                response = client.get(current_url)
                response.raise_for_status()
            except httpx.HTTPError as err:
                print(f"Network error on {current_url}: {err}")
                break

            books, next_url = parse_page(response.text, current_url)
            all_books.extend(books)

            current_url = next_url
            page_count += 1
            time.sleep(1)

    save_book(all_books)
    count, avg_price = fetch_summary()
    print(f"Stored {count} books in database. Average price: £{avg_price:.2f}")


if __name__ == "__main__":
    main()
