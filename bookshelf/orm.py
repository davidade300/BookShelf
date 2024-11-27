from sqlalchemy import ForeignKey, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import registry, relationship
from bookshelf.model import Book, Category

mapper_registry = registry()

metadata = MetaData()

tb_books = Table(
    "tb_books",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String, nullable=False),
    Column("language", String, nullable=False),
    Column("isbn", Integer, unique=True, nullable=False),
    Column("status", String, nullable=False),
)

tb_category = Table(
    "tb_categories",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
    Column("book_isbn", Integer, ForeignKey("tb_books.isbn"), nullable=False),
)


def start_mappers():
    mapper_registry.map_imperatively(Book, tb_books)
    mapper_registry.map_imperatively(
        Category,
        tb_category,
        properties={
            "book": relationship(Book, foreign_keys=[Category.book_isbn])
        },
    )
