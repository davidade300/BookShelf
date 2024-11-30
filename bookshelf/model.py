from dataclasses import dataclass
from enum import Enum


class Status(Enum):
    NOT_STARTED = "não iniciado"
    ONGOING = "em andamento"
    FINISHED = "finalzado"
    SUSPENDED = "pausado"
    INTERRUPTED = "suspenso por prazo indefinido"


@dataclass(unsafe_hash=True)
class Category:
    name: str


# TODO: if necessary to make the class iterable, just implement the __iter__() method
class Book:
    def __init__(
        self,
        title: str,
        language: str,
        isbn: int,
        status: Status = Status.NOT_STARTED,
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
