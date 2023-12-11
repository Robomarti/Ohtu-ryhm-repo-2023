# RUN TESTS OUTSIDE POETRY SHELL WITH COMMAND:
# FLASK_ENV=test poetry run pytest
# RUN COVERAGE IN POETRY SHELL:
# FLASK_ENV=test coverage run --branch -m pytest

import sys
import os

# The following paths atre needed for tests to see app.py.
# This will need to be updated if project folder structure is changed.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import unittest
from flask import session
from src.app import app  
import sources
import in_memory_db

class SourcesTestCase(unittest.TestCase):
    def setUp(self):
        app.config["SECRET_KEY"] = 'testkey1testkey2testkey3testkey4' # For some reason could not get .env work here?
        app.test_request_context().push()

        with app.test_request_context():

            in_memory_db.setup_db()


    def tearDown(self):
        in_memory_db.empty_db()



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

    def test_delete_book(self):
        with app.test_request_context():
            session["user_id"] = 1
            result = sources.delete_source("books", 1)
            self.assertEqual(result, True)

            data = sources.get_all_books()
            self.assertEqual(
                data,
                [(2, 
                 1, 
                 'Book Tester 2', 
                 'Testbook2', 
                 'Testbook Publishing Co.', 
                 'Testbook address', 
                 2020)])

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

    def test_delete_article(self):
        with app.test_request_context():
            session["user_id"] = 1
            result = sources.delete_source("articles", 1)
            self.assertEqual(result, True)

            data = sources.get_all_articles()
            self.assertEqual(
                data,
                [(2, 
                  1, 
                  'Test Article Writer 2', 
                  'Test article 2', 
                  'Article journal 2', 
                  1992, 
                  'Volume 2', 
                  12, 
                  '20-25')])

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
    
    def test_delete_inproceeding(self):
        with app.test_request_context():
            session["user_id"] = 1
            result = sources.delete_source("inproceedings", 1)
            self.assertEqual(result, True)

            data = sources.get_all_inproceedings()
            self.assertEqual(
                data,
                [(2,
                1,
                'Author2',
                'Inproceedings no. 2',
                'Book 2 of inproceedings',
                'Serie 2',
                2002,
                '200',
                'Publisher no. 2',
                'Address no. 2')])

if __name__ == '__main__':
    unittest.main()
