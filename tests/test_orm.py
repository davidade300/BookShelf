from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from bookshelf.model import Book, Status
import pytest
from bookshelf.orm import metadata, start_mappers


@pytest.fixture(scope="function")
def session():
    engine = create_engine(
        "sqlite:///:memory:", connect_args={"check_same_thread": False}
    )

    metadata.create_all(engine, checkfirst=True)
    start_mappers()
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

    # TODO: fix this test


# def test_category_mapper_can_load_category(session): ...


# TODO: Write this test
# def test_can_return_book_using_tb_categories_isbn(session): ...
