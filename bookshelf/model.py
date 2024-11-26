from dataclasses import dataclass
from enum import Enum


class Status(Enum):
    NOT_STARTED = "não iniciado"
    ONGOING = "em andamento"
    FINISHED = "finalzado"
    SUSPENDED = "pausado"
    INTERRUPTED = "suspenso por prazo indefinido"


class Book:
    def __init__(
        self,
        title: str,
        language: str,
        isbn: str,
        status: Status = Status.NOT_STARTED,
    ) -> None:
        self.title = title
        self.language = language
        self.isbn = isbn
        self.status = status


@dataclass
class Category:
    name: str
    books: set[Book] = set()
