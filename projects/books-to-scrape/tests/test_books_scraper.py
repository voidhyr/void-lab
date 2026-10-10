from fundamentals.scrapers.books_toscrape.scraper import (
    clean_price,
    parse_rating,
)


def test_clean_price_standard():
    assert clean_price("£51.44") == 51.44
    assert clean_price("£10.00") == 10.0


def test_clean_price_with_whitespace():
    assert clean_price("  £9.99 \n") == 9.99


def test_parse_rating_valid_words():
    assert parse_rating("One") == 1
    assert parse_rating("Three") == 3
    assert parse_rating("Five") == 5


def test_parse_rating_fallback_for_unknown():
    assert parse_rating("Unknown") == 0
    assert parse_rating("") == 0
