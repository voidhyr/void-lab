import httpx
from bs4 import BeautifulSoup
from urllib.parse import  urljoin

url = "https://books.toscrape.com/"

header = {
"User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
}

response = httpx.get(url, headers = header)

soup = BeautifulSoup(response.text, "html.parser")
print(response.status_code)

all_books = []

books = soup.find_all("article", class_ = "product_pod")
#print(len(books))
for book in books:
    h3_tag = book.find("h3")
    if h3_tag:
        a_tag = h3_tag.find("a")
        title = a_tag["title"]
        link = a_tag["href"]
        full_link = urljoin(url, link)
        # print(title)
        # print(link)

    price_tag = book.find("p", class_ = "price_color")
    price = price_tag.text
    price = price.replace("£", "")
    price = float(price)
    # print(type(price))


    rating_tag = book.find("p", class_ = "star-rating")
    rating_word = rating_tag.get("class", [])
    stock_tag = book.find("p", class_ = "instock availability")
    stock_status = stock_tag.text
    stock_status = stock_status.strip()

    # print(rating_word)
    # print(stock_status)
    rating_word = rating_word[1]
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    rating_num = rating_map.get(rating_word, 0)
    # print(rating_num)


    book_dict = {"title":title, "link":full_link, "price":price, "rating":rating_num, "stock":stock_status}
    all_books.append(book_dict)



print(len(all_books))
for book in all_books:
    print(book)

