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
            ('DDD', 'Portuguese', 9788550800653, 'em andamento');"
        )
    )

    session.commit()

    expected = [Book("DDD", "Portuguese", 9788550800653, Status.ONGOING.value)]

    assert session.query(Book).all() == expected


def test_category_mapper_can_load_category(session):
    session.execute(
        text(
            "INSERT INTO tb_categories (name) VALUES ('Software Development');"
        )
    )

    session.commit()

    expected = [Category("Software Development")]

    assert session.query(Category).all() == expected


# TODO: Write this test
def test_can_return_book_using_tb_book_categories_book_isbn(session):
    session.execute(
        text(
            "INSERT INTO tb_books (title, language, isbn, status) VALUES  \
            ('DDD', 'Portuguese', 9788550800653, 'em andamento');"
        )
    )

    session.execute(
        text(
            "INSERT INTO tb_categories (name) VALUES \
            ('Software Development');"
        )
    )

    book_isbn = session.execute(
        text("SELECT isbn FROM tb_books WHERE isbn = 9788550800653")
    ).fetchone()[0]

    category_name = session.execute(
        text(
            "SELECT name FROM tb_categories WHERE name = 'Software Development'"
        )
    ).fetchone()[0]

    session.execute(
        text(
            "INSERT INTO tb_book_categories (book_isbn, category_name) VALUES (:book_isbn, :category_name);"
        ),
        {"book_isbn": book_isbn, "category_name": category_name},
    )

    session.commit()

    books_in_category = session.execute(
        text(
            "SELECT b.title, b.language, b.isbn, b.status \
             FROM tb_books b \
             JOIN tb_book_categories bc ON b.isbn = bc.book_isbn \
             JOIN tb_categories c ON bc.category_name = c.name \
             WHERE c.name = 'Software Development';"
        )
    ).fetchall()

    assert any(book[0] == "DDD" for book in books_in_category)
