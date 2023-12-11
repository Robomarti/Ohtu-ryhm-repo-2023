from sqlalchemy.sql import text
from flask import session
import sys

from src.db import db

# we need all of the arguments
# pylint: disable=too-many-arguments
def add_article(article_author,
                article_title,
                article_journal,
                article_year,
                article_volume,
                article_number,
                article_pages):

    if session.get("user_id") is None:
        return False
    user_id = session["user_id"]

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
                    :user_id,
                    :article_author, 
                    :article_title,
                    :article_journal,
                    :article_year,
                    :article_volume,
                    :article_number,
                    :article_pages
                )""")

    try:
        db.session.execute(sql, {
                    "user_id": int(user_id),
                    "article_author": article_author,
                    "article_title": article_title,
                    "article_journal": article_journal,
                    "article_year": int(article_year),
                    "article_volume": article_volume,
                    "article_number": int(article_number),
                    "article_pages": article_pages
                    }
                )
        db.session.commit()

    # we disable this for now since we don't yet know what kind of
    # exceptions we should expect:
    # pylint: disable=broad-except
    except Exception as exception:
        print("sources.py -> add_article: " , exception, file=sys.stderr)
        return False
    return True

def add_book(book_author,
             book_title,
             book_publisher,
             book_address,
             book_year):

    if session.get("user_id") is None:
        return False

    user_id = session["user_id"]
    sql = text("""INSERT INTO books (
                    user_id,
                    book_author,
                    book_title,
                    book_publisher,
                    book_address,
                    book_year
                ) 
                VALUES (
                    :user_id,
                    :book_author,
                    :book_title,
                    :book_publisher,
                    :book_address,
                    :book_year
                )""")

    try:
        db.session.execute(sql, {
                    "user_id": int(user_id),
                    "book_author": book_author,
                    "book_title": book_title,
                    "book_publisher": book_publisher,
                    "book_address": book_address,
                    "book_year": int(book_year)
                    }
                )
        db.session.commit()
    # pylint: disable=broad-except
    except Exception as exception:
        print("sources.py -> add_book: Exception: ",  exception, file=sys.stderr)
        return False
    return True

# pylint: disable=too-many-arguments
def add_inproceedings(inproceedings_author,
                      inproceedings_title,
                      inproceedings_booktitle,
                      inproceedings_series,
                      inproceedings_year,
                      inproceedings_pages,
                      inproceedings_publisher,
                      inproceedings_address):

    if session.get("user_id") is None:
        return False

    user_id = session["user_id"]
    sql = text("""INSERT INTO inproceedings (
                    user_id,
                    inproceedings_author,
                    inproceedings_title,
                    inproceedings_booktitle,
                    inproceedings_series,
                    inproceedings_year,
                    inproceedings_pages,
                    inproceedings_publisher,
                    inproceedings_address
                ) 
                VALUES (
                    :user_id,
                    :inproceedings_author,
                    :inproceedings_title,
                    :inproceedings_booktitle,
                    :inproceedings_series,
                    :inproceedings_year,
                    :inproceedings_pages,
                    :inproceedings_publisher,
                    :inproceedings_address
                )""")

    try:
        db.session.execute(sql, {
                    "user_id": int(user_id),
                    "inproceedings_author": inproceedings_author,
                    "inproceedings_title": inproceedings_title,
                    "inproceedings_booktitle": inproceedings_booktitle,
                    "inproceedings_series": inproceedings_series,
                    "inproceedings_year": int(inproceedings_year),
                    "inproceedings_pages": inproceedings_pages,
                    "inproceedings_publisher": inproceedings_publisher,
                    "inproceedings_address": inproceedings_address
                    }
                )
        db.session.commit()
    # pylint: disable=broad-except
    except Exception as exception:
        print("sources.py -> add_article:", exception, file=sys.stderr)
        return False
    return True

def get_all_articles():
    user_id = session.get("user_id")
    if not user_id:
        return False

    user_id = session["user_id"]
    sql = text("""SELECT
                    id,
                    user_id,
                    article_author, 
                    article_title, 
                    article_journal, 
                    article_year, 
                    article_volume, 
                    article_number,
                    article_pages
               FROM articles
               WHERE user_id=:user_id
               """)

    result = db.session.execute(sql, {"user_id": user_id})
    articles_by_user = result.fetchall()
    return articles_by_user

def get_all_books():
    if session.get("user_id") is None:
        return False

    user_id = session["user_id"]
    sql = text("""SELECT
                    id,
                    user_id,
                    book_author, 
                    book_title,
                    book_publisher,
                    book_address,
                    book_year
               FROM books
               WHERE user_id=:user_id
               """)

    result = db.session.execute(sql, {"user_id": user_id})
    books_by_user = result.fetchall()
    return books_by_user

def get_all_inproceedings():
    if session.get("user_id") is None:
        return False
    user_id = session["user_id"]

    sql = text("""SELECT
                    id,
                    user_id,
                    inproceedings_author, 
                    inproceedings_title,
                    inproceedings_booktitle,
                    inproceedings_series,
                    inproceedings_year, 
                    inproceedings_pages,
                    inproceedings_publisher,
                    inproceedings_address
               FROM inproceedings
               WHERE user_id=:user_id
               """)

    result = db.session.execute(sql, {"user_id": user_id})
    inproceedings_by_user = result.fetchall()
    return inproceedings_by_user


def delete_source(source_type, source_id):
    if session.get("user_id") is None:
        return False

    user_id = session["user_id"]
    allowed_source_types = ['books', 'articles', 'inproceedings']
    if source_type not in allowed_source_types:
        return False

    sql = text(f"DELETE FROM {source_type} WHERE (id = :id AND user_id=:user_id);")
    try:
        db.session.execute(sql, {"id": str(source_id), "user_id": str(user_id)})
        db.session.commit()
    # pylint: disable=broad-except
    except Exception as exception:
        print("sources.py -> delete_source:", exception, file=sys.stderr)
        return False
    return True
