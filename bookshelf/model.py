from enum import Enum


class Status(Enum):
    NOT_STARTED = "não iniciado"
    ONGOING = "em andamento"
    FINISHED = "finalzado"
    SUSPENDED = "pausado"
    INTERRUPTED = "suspenso por prazo indefinido"


# @dataclass(unsafe_hash=True)
# class Category:
# name: str


class Category:
    def __init__(self, name: str, book_isbn: int) -> None:
        self.name = name
        self.book_isbn = book_isbn

    def __eq__(self, other) -> bool:
        if not isinstance(other, Category):
            return False
        return other.book_isbn == self.book_isbn and other.name == self.name

    def __hash__(self) -> int:
        return hash(self.name.casefold())


# TODO: if necessary to make the class iterable, just implement the __iter__() method
class Book:
    def __init__(
        self,
        title: str,
        language: str,
        isbn: int,
        status: str = Status.NOT_STARTED.value,
        categories: set[Category] | None = set(),
    ) -> None:
        self.title = title
        self.language = language
        self.isbn = isbn
        self.status = status
        self.categories = categories

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return False
        return other.isbn == self.isbn

    def __hash__(self) -> int:
        return hash(self.isbn)
