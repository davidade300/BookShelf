from bookshelf.model import Book, Status


def test_creating_book_with_empty_status():
    empty_status_book = Book("DDD", "Portuguese", 9788550800653)

    assert empty_status_book.status is Status.NOT_STARTED
