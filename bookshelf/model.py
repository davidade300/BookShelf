from typing import List
from enum import Enum


class Status(Enum):
    NOT_STARTED = "não iniciado"
    ONGOING = "em andamento"
    FINISHED = "finalzado"
    SUSPENDED = "pausado"
    INTERRUPTED = "suspenso por prazo indefinido"


class Book:
    # TODO: verificar necessidade de criar uma classe para categoria e para status
    def __init__(
        self,
        titulo: str,
        idioma: str,
        isbn: str,
        categoria: List[str] = [],
        status: Status = Status.NOT_STARTED,
    ) -> None: ...
