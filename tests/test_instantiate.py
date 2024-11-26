import pytest  # noqa: F401
from bookshelf.model import Book, Status


def test_creating_book_with_empty_status():
    empty_status_book = Book(
        "title",
        "portugues",
        "213456987",
    )

    assert empty_status_book.status is Status.NOT_STARTED


def test_creating_book_with_multiple_category_values():
    multiple_category_book = Book(
        "title",
        "portugues",
        "213456987",
    )

    assert multiple_category_book.category == ("cat_1", "cat_2")
