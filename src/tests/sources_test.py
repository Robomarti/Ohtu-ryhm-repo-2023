# RUN TESTS OUTSIDE POETRY SHELL WITH COMMAND:
# FLASK_ENV=test poetry run pytest
# RUN COVERAGE IN POETRY SHELL:
# FLASK_ENV=test coverage run --branch -m pytest
# coverage report -m pytest tests/sources_test.py

import sys
import os

# If the following mess is not here, tests will not see app.py!!
# This will probably break if project folder structure is changed.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import unittest
from flask import session
from sqlalchemy.sql import text
from src.app import app  
from src.db import db 
import sources

class YourTestCase(unittest.TestCase):
    def setUp(self):
        app.config["SECRET_KEY"] = 'testkey1testkey2testkey3testkey4' # For some reason could not get .env work here?
        app.test_request_context().push()

        with app.test_request_context():

            # Initialise test database for books:
            try: 
                sql = text("""CREATE TABLE books (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id INT,
                                book_author TEXT, 
                                book_title TEXT,
                                book_publisher TEXT,
                                book_address TEXT,
                                book_year INT
                            );""")
                db.session.execute(sql)

                sql = text("""INSERT INTO books (
                                user_id,
                                book_author,
                                book_title,
                                book_publisher,
                                book_address,
                                book_year) 
                            VALUES (
                                1,
                                'Book Tester 1',
                                'Testbook',
                                'Testbook Publishing Co.',
                                'Testbook address',
                                2000
                            );""")
                db.session.execute(sql)

                sql = text("""INSERT INTO books (
                                user_id,
                                book_author,
                                book_title,
                                book_publisher,
                                book_address,
                                book_year)
                            VALUES (
                                1,
                                'Book Tester 2',
                                'Testbook2',
                                'Testbook Publishing Co.',
                                'Testbook address',
                                2020)
                            ;""")
                db.session.execute(sql)
                db.session.commit()
            except Exception as exception:
                print("sources_test.py -> setUp books: Exception: ", exception)
            
            # Initialise test database for articles:
            try: 
                sql = text("""CREATE TABLE articles (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id INT,
                                article_author TEXT, 
                                article_title TEXT,
                                article_journal TEXT,
                                article_year INT, 
                                article_volume TEXT,
                                article_number INT,
                                article_pages TEXT
                            );""")
                db.session.execute(sql)

                sql = text("""INSERT INTO articles (
                                user_id,
                                article_author,
                                article_title,
                                article_journal,
                                article_year,
                                article_volume,
                                article_number,
                                article_pages)
                           VALUES (
                                1,
                                'Test Article Writer 1',
                                'Test article 1',
                                'Article journal 1',
                                1991,
                                'Volume 1',
                                11,
                                '10-15'
                            );""")
                db.session.execute(sql)

                sql = text("""INSERT INTO articles (
                                user_id,
                                article_author,
                                article_title,
                                article_journal,
                                article_year,
                                article_volume,
                                article_number,
                                article_pages)
                           VALUES (
                                1,
                                'Test Article Writer 2',
                                'Test article 2',
                                'Article journal 2',
                                1992,
                                'Volume 2',
                                12,
                                '20-25'
                            );""")
                db.session.execute(sql)
                db.session.commit()

            except Exception as exception:
                print("sources_test.py -> setUp articles: Exception: ", exception)

            # Initialise test database for inproceedings
            try:
                sql = text("""CREATE TABLE inproceedings (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id INT,
                                inproceedings_author TEXT, 
                                inproceedings_title TEXT,
                                inproceedings_booktitle TEXT,
                                inproceedings_series TEXT,
                                inproceedings_year INT, 
                                inproceedings_pages TEXT,
                                inproceedings_publisher TEXT,
                                inproceedings_address TEXT
                            );""")
                db.session.execute(sql)
                sql = text("""INSERT INTO inproceedings (
                                user_id,
                                inproceedings_author, 
                                inproceedings_title,
                                inproceedings_booktitle,
                                inproceedings_series,
                                inproceedings_year, 
                                inproceedings_pages,
                                inproceedings_publisher,
                                inproceedings_address)
                            VALUES (
                                1,
                                'Author1',
                                'Inproceedings no. 1',
                                'Book 1 of inproceedings',
                                'Serie 1',
                                2001,
                                '100',
                                'Publisher no. 1',
                                'Address no. 1'
                            );""")
                db.session.execute(sql)
                sql = text("""INSERT INTO inproceedings (
                                user_id,
                                inproceedings_author, 
                                inproceedings_title,
                                inproceedings_booktitle,
                                inproceedings_series,
                                inproceedings_year, 
                                inproceedings_pages,
                                inproceedings_publisher,
                                inproceedings_address)
                            VALUES (
                                1,
                                'Author2',
                                'Inproceedings no. 2',
                                'Book 2 of inproceedings',
                                'Serie 2',
                                2002,
                                '200',
                                'Publisher no. 2',
                                'Address no. 2'
                            );""")
                db.session.execute(sql)
            except Exception as exception:
                print("sources_test.py -> setUp : Exception: ", exception)

    def tearDown(self):
        try: 
            sql = text("DROP TABLE books;")
            db.session.execute(sql)
            sql = text("DROP TABLE articles;")
            result = db.session.execute(sql)
            sql = text("DROP TABLE inproceedings;")
            result = db.session.execute(sql)
            db.session.commit()
            print("sources_test / tearDown: result =", result)
        except Exception as exception:
            print("sources_test.py -> tearDown: Exception: ", exception)
            

    # Tests for books:
    def test_get_all_books(self):
        with app.test_request_context():
            session["user_id"] = 1
            data = sources.get_all_books()
            self.assertEqual(
                data,
                [(1, 
                  1, 
                  'Book Tester 1', 
                  'Testbook', 
                  'Testbook Publishing Co.', 
                  'Testbook address', 
                  2000),
                (2, 
                 1, 
                 'Book Tester 2', 
                 'Testbook2', 
                 'Testbook Publishing Co.', 
                 'Testbook address', 
                 2020)])
    def test_get_all_books_when_not_login(self):
        with app.test_request_context():
            data = sources.get_all_books()
            self.assertEqual(data, False)

    def test_add_book(self):
        with app.test_request_context():
            session["user_id"] = 1
            result = sources.add_book(
                'Book Tester 3', 
                'Testbook3', 
                'Testbook Publishing Co.', 
                'Testbook address3', 
                2023)
            self.assertEqual(result, True)
            data = sources.get_all_books()
            self.assertEqual(len(data), 3)
            self.assertEqual(
                data[2], 
                (3, 
                 1, 
                 'Book Tester 3', 
                 'Testbook3', 
                 'Testbook Publishing Co.', 
                 'Testbook address3', 
                 2023))

    def test_add_book_when_not_login(self):
        with app.test_request_context():
            result = sources.add_book(
                'Book Tester 3', 
                'Testbook3', 
                'Testbook Publishing Co.', 
                'Testbook address3', 
                2023)
            self.assertEqual(result, False)

    # Tests for articles:
    def test_get_all_articles(self):
        with app.test_request_context():
            session["user_id"] = 1
            data = sources.get_all_articles()
            self.assertEqual(
                data, 
                [(1, 
                  1, 
                  'Test Article Writer 1', 
                  'Test article 1', 
                  'Article journal 1', 
                  1991, 
                  'Volume 1', 
                  11, 
                  '10-15'), 
                 (2, 
                  1, 
                  'Test Article Writer 2', 
                  'Test article 2', 
                  'Article journal 2', 
                  1992, 
                  'Volume 2', 
                  12, 
                  '20-25')])

    def test_get_all_articles_when_not_login(self):
        with app.test_request_context():
            data = sources.get_all_articles()
            self.assertEqual(data, False)

    def test_add_article(self):
        with app.test_request_context():
            session["user_id"] = 1
            result = sources.add_article(
                'Test Article Writer 3', 
                'Test article 3', 
                'Article journal 3', 
                1993, 
                'Volume 3', 
                13, 
                '30-35')
            self.assertEqual(result, True)
            data = sources.get_all_articles()
            self.assertEqual(len(data), 3)
            self.assertEqual(
                data[2], 
                (3, 
                 1, 
                 'Test Article Writer 3', 
                 'Test article 3', 
                 'Article journal 3', 
                 1993, 
                 'Volume 3', 
                 13, 
                 '30-35'))

    def test_add_article_when_not_login(self):
        with app.test_request_context():
            result = sources.add_article(
                'Test Article Writer 3', 
                'Test article 3', 
                'Article journal 3', 
                1993, 
                'Volume 3', 
                13, 
                '30-35')
            self.assertEqual(result, False)

    # Tests for inproceedings:
    def test_get_all_inproceedings(self):
        with app.test_request_context():
            session["user_id"] = 1
            data = sources.get_all_inproceedings()
            self.assertEqual(
                data, 
                [(1,
                1,
                'Author1',
                'Inproceedings no. 1',
                'Book 1 of inproceedings',
                'Serie 1',
                2001,
                '100',
                'Publisher no. 1',
                'Address no. 1'), 
                (2,
                1,
                'Author2',
                'Inproceedings no. 2',
                'Book 2 of inproceedings',
                'Serie 2',
                2002,
                '200',
                'Publisher no. 2',
                'Address no. 2')])

    def test_get_all_inproceedings_when_not_login(self):
        with app.test_request_context():
            data = sources.get_all_inproceedings()
            self.assertEqual(data, False)

    def test_add_inproceedings(self):
        with app.test_request_context():
            session["user_id"] = 1
            result = sources.add_inproceedings(
                                'Author3',
                                'Inproceedings no. 3',
                                'Book 3 of inproceedings',
                                'Serie 3',
                                2003,
                                '300',
                                'Publisher no. 3',
                                'Address no. 3')
            self.assertEqual(result, True)
            data = sources.get_all_inproceedings()
            self.assertEqual(len(data), 3)
            self.assertEqual(
                    data[2], 
                    (3,
                    1,
                    'Author3',
                    'Inproceedings no. 3',
                    'Book 3 of inproceedings',
                    'Serie 3',
                    2003,
                    '300',
                    'Publisher no. 3',
                    'Address no. 3'))

    def test_add_inproceedings_when_not_login(self):
        with app.test_request_context():
            result = sources.add_inproceedings(
                                'Author3',
                                'Inproceedings no. 3',
                                'Book 3 of inproceedings',
                                'Serie 3',
                                2003,
                                '300',
                                'Publisher no. 3',
                                'Address no. 3')
            self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
