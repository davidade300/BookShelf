from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, clear_mappers
from bookshelf.model import Book, Category, Status
import pytest
from bookshelf.orm import metadata, start_mappers


@pytest.fixture(scope="function")
def session():
    clear_mappers()  # this fixes the errors
    start_mappers()

    engine = create_engine(
        "sqlite:///:memory:", connect_args={"check_same_thread": True}
    )

    metadata.create_all(engine, checkfirst=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.close()


def test_book_mapper_can_load_books(session):
    session.execute(
        text(
            "INSERT INTO tb_books (title, language, isbn, status) VALUES \
        ('livro','asdf', 1234123,'não iniciado') ;"
        )
    )

    session.commit()

    expected = [Book("livro", "asdf", 1234123, Status.NOT_STARTED.value)]

    assert session.query(Book).all() == expected


def test_category_mapper_can_load_category(session):
    session.execute(
        text(
            "INSERT INTO tb_categories (name, book_isbn) VALUES ('Software Development', 1234123) ;"
        )
    )

    session.commit()

    expected = [Category("Software Development", 1234123)]

    assert session.query(Category).all() == expected


# TODO: Write this test
# def test_can_return_book_using_tb_categories_isbn(session): ...
