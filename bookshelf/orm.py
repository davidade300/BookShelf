from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.orm import registry
from bookshelf.model import Book

mapper_registry = registry()

metadata = MetaData()

tb_book = Table(
    "tb_book",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(60), nullable=False),
    Column("language", String, nullable=False),
    Column("isbn", String, unique=True, nullable=False),
    Column("status", String, nullable=False),
)


def start_mappers():
    mapper_registry.map_imperatively(Book, tb_book)
