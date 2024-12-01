from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    UniqueConstraint,
)
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

tb_categories = Table(
    "tb_categories",
    metadata,
    Column("name", String(255), primary_key=True, nullable=False, unique=True),
)

tb_book_categories = Table(
    "tb_book_categories",
    metadata,
    Column(
        "book_isbn",
        Integer,
        ForeignKey("tb_books.isbn"),
        nullable=False,
    ),
    Column(
        "category_name",
        String,
        ForeignKey("tb_categories.name"),
        nullable=False,
    ),
    UniqueConstraint("book_isbn", "category_name"),
)


def start_mappers():
    mapper_registry.map_imperatively(Category, tb_categories)
    mapper_registry.map_imperatively(
        Book,
        tb_books,
        properties={
            "categories": relationship(
                Category,
                secondary=tb_book_categories,
            )
        },
    )
