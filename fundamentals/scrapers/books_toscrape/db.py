import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "books.db"


def init_db() -> None:
    query = """CREATE TABLE IF NOT EXISTS books
               (
                   id
                   INTEGER
                   PRIMARY
                   KEY
                   AUTOINCREMENT,
                   title
                   TEXT
                   NOT
                   NULL,
                   link
                   TEXT
                   UNIQUE
                   NOT
                   NULL,
                   price
                   REAL
                   NOT
                   NULL,
                   rating
                   INTEGER
                   NOT
                   NULL,
                   stock
                   TEXT
                   NOT
                   NULL
               );
            """
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(query)


def save_book(books: list[dict]):
    insert_query = """
                   INSERT INTO books (title, link, price, rating, stock)
                   VALUES (?, ?, ?, ?, ?) ON CONFLICT (link) DO
                   UPDATE SET price = excluded.price, rating = excluded.rating, stock = excluded.stock
                   """
    book_tuples = [
        (b["title"], b["link"], b["price"], b["rating"], b["stock"]) for b in books
    ]
    with sqlite3.connect(DB_PATH) as conn:
        conn.executemany(insert_query, book_tuples)


def fetch_summary():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT count(*), AVG(price) FROM books;")
        count, avg_price = cursor.fetchone()
        return count, avg_price or 0.0
