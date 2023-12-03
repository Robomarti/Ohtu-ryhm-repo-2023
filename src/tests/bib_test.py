import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import unittest
from src.app import app
from unittest.mock import Mock, patch
import bib

class TestBib(unittest.TestCase):
    def setUp(self):
        app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    @patch('bib.sources.get_all_articles')
    def test_return_all_articles(self, mock_get_all_articles):
        mock_article = Mock()
        mock_article.id = 1
        mock_article.article_author = "Author"
        mock_article.article_title = "Title"
        mock_article.article_journal = "Journal"
        mock_article.article_year = 2023
        mock_article.article_volume = "volume"
        mock_article.article_number = "number"
        mock_article.article_pages = "pages"

        mock_get_all_articles.return_value = [mock_article]

        result = bib.return_all_articles()

        expected_result = [(f"@article{{ {mock_article.id},\n" \
                         f"  author = \"{mock_article.article_author}\",\n" \
                         f"  title = \"{mock_article.article_title}\",\n" \
                         f"  journal = \"{mock_article.article_journal}\",\n" \
                         f"  year = {mock_article.article_year},\n" \
                         f"  volume = \"{mock_article.article_volume}\",\n" \
                         f"  number = \"{mock_article.article_number}\",\n" \
                         f"  pages = \"{mock_article.article_pages}\"\n" \
                         f"}}\n", mock_article.id)]

        self.assertEqual(result, expected_result)

    @patch('bib.sources.get_all_articles')
    def test_return_no_articles(self, mock_get_all_articles):
        mock_article = Mock()
        mock_article.id = 1
        mock_article.article_author = "Author"
        mock_article.article_title = "Title"
        mock_article.article_journal = "Journal"
        mock_article.article_year = 2023
        mock_article.article_volume = "volume"
        mock_article.article_number = "number"
        mock_article.article_pages = "pages"

        mock_get_all_articles.return_value = False

        result = bib.return_all_articles()

        expected_result = []

        self.assertEqual(result, expected_result)

    @patch('bib.sources.get_all_books')
    def test_return_all_books(self, mock_get_all_books):
        mock_book = Mock()
        mock_book.id = 1
        mock_book.book_author = "Author"
        mock_book.book_title = "Title"
        mock_book.book_publisher = "Publisher"
        mock_book.book_address = "Address"
        mock_book.book_year = 2023

        mock_get_all_books.return_value = [mock_book]

        result = bib.return_all_books()

        expected_result = [(f"@book{{ {mock_book.id},\n" \
                      f"  author = \"{mock_book.book_author}\",\n" \
                      f"  title = \"{mock_book.book_title}\",\n" \
                      f"  publisher = \"{mock_book.book_publisher}\",\n" \
                      f"  address = \"{mock_book.book_address}\",\n" \
                      f"  year = {mock_book.book_year}\n" \
                      f"}}\n", mock_book.id)]

        self.assertEqual(result, expected_result)

    @patch('bib.sources.get_all_books')
    def test_return_no_books(self, mock_get_all_books):
        mock_book = Mock()
        mock_book.id = 1
        mock_book.book_author = "Author"
        mock_book.book_title = "Title"
        mock_book.book_publisher = "Publisher"
        mock_book.book_address = "Address"
        mock_book.book_year = 2023

        mock_get_all_books.return_value = False

        result = bib.return_all_books()

        expected_result = []

        self.assertEqual(result, expected_result)

    @patch('bib.sources.get_all_inproceedings')
    def test_return_all_inproceeding(self, mock_get_all_inproceedings):
        mock_inproceeding = Mock()
        mock_inproceeding.id = 1
        mock_inproceeding.inproceedings_author = "Author"
        mock_inproceeding.inproceedings_title = "Title"
        mock_inproceeding.inproceedings_booktitle = "Booktitle"
        mock_inproceeding.inproceedings_series = "Series"
        mock_inproceeding.inproceedings_year = 2023
        mock_inproceeding.inproceedings_pages = "pages"
        mock_inproceeding.inproceedings_publisher = "Publisher"
        mock_inproceeding.inproceedings_address = "Address"

        mock_get_all_inproceedings.return_value = [mock_inproceeding]

        result = bib.return_all_inproceedings()

        expected_result = [(f"@inproceedings{{ {mock_inproceeding.id},\n" \
                              f"  author = \"{mock_inproceeding.inproceedings_author}\",\n" \
                              f"  title = \"{mock_inproceeding.inproceedings_title}\",\n" \
                              f"  booktitle = \"{mock_inproceeding.inproceedings_booktitle}\",\n" \
                              f"  series = \"{mock_inproceeding.inproceedings_series}\",\n" \
                              f"  year = {mock_inproceeding.inproceedings_year},\n" \
                              f"  pages = \"{mock_inproceeding.inproceedings_pages}\",\n" \
                              f"  publisher = \"{mock_inproceeding.inproceedings_publisher}\",\n" \
                              f"  address = \"{mock_inproceeding.inproceedings_address}\"\n" \
                              f"}}\n", mock_inproceeding.id)]

        self.assertEqual(result, expected_result)

    @patch('bib.sources.get_all_inproceedings')
    def test_return_no_inproceeding(self, mock_get_all_inproceedings):
        mock_inproceeding = Mock()
        mock_inproceeding.id = 1
        mock_inproceeding.inproceedings_author = "Author"
        mock_inproceeding.inproceedings_title = "Title"
        mock_inproceeding.inproceedings_booktitle = "Booktitle"
        mock_inproceeding.inproceedings_series = "Series"
        mock_inproceeding.inproceedings_year = 2023
        mock_inproceeding.inproceedings_pages = "pages"
        mock_inproceeding.inproceedings_publisher = "Publisher"
        mock_inproceeding.inproceedings_address = "Address"

        mock_get_all_inproceedings.return_value = False

        result = bib.return_all_inproceedings()

        expected_result = []

        self.assertEqual(result, expected_result)
