import time
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup

rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
current_url = "https://books.toscrape.com/"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
}

all_books = []
page_count = 0

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
        price = price_tag.text
        price = price.replace("£", "")
        price = float(price)
        # print(type(price))

        rating_tag = book.find("p", class_="star-rating")
        rating_word = rating_tag.get("class", [])
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
for book in all_books:
    print(book)
