from dataclasses import dataclass
from enum import Enum
from typing import Set


class Status(Enum):
    NOT_STARTED = "não iniciado"
    ONGOING = "em andamento"
    FINISHED = "finalzado"
    SUSPENDED = "pausado"
    INTERRUPTED = "suspenso por prazo indefinido"


@dataclass(frozen=True)
class Category:
    name: str


class Book:
    def __init__(
        self,
        title: str,
        language: str,
        isbn: str,
        category: Set[Category],
        status: Status = Status.NOT_STARTED,
    ) -> None:
        self.title = title
        self.language = language
        self.isbn = isbn
        self.category = category
        self.status = status
