from db import db
from sqlalchemy.sql import text
from flask import session



def add_article(article_author: str, 
                article_title: str, 
                article_journal: str, 
                article_year: int, 
                article_volume: str, 
                article_number: int, 
                article_pages: str):
    
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
                    article_pages

                ) 
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
                    "user_id": user_id,
                    "article_author": article_author, 
                    "article_title": article_title,
                    "article_journal": article_journal,
                    "article_year": str(article_year),
                    "article_volume": article_volume,
                    "article_number": str(article_number),
                    "article_pages": article_pages
                    }
                )
        db.session.commit()
    except Exception as exception:
        print("sources.py -> add_article: " , exception)
        return False
    
    return True

def add_book(book_author: str, 
             book_title: str, 
             book_publisher: str, 
             book_address: str, 
             book_year: int):
    
    if session.get("user_id") is None:
        return False
    user_id = session["user_id"]

    print("sources.py / add_book! author = ", book_author)
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
                    "user_id": user_id,
                    "book_author": book_author, 
                    "book_title": book_title,
                    "book_publisher": book_publisher,
                    "book_address": book_address,
                    "book_year": str(book_year)
                    }
                )
        db.session.commit()
    except Exception as exception:
        print("sources.py -> add_book: Exception: ",  exception)
        return False
    
    return True

def add_inproceedings(inproceedings_author: str, 
                      inproceedings_title: str, 
                      inproceedings_booktitle: str, 
                      inproceedings_series: str, 
                      inproceedings_year: int, 
                      inproceedings_pages: str, 
                      inproceedings_publisher: str, 
                      inproceedings_address: str):
    if session.get("user_id") is None:
        return False
    user_id = session["user_id"]

    print("sources.py / add! author = ", inproceedings_author)
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
                    "user_id": user_id,
                    "inproceedings_author": inproceedings_author,
                    "inproceedings_title": inproceedings_title,
                    "inproceedings_booktitle": inproceedings_booktitle,
                    "inproceedings_series": inproceedings_series,
                    "inproceedings_year": str(inproceedings_year),
                    "inproceedings_pages": inproceedings_pages,
                    "inproceedings_publisher": inproceedings_publisher,
                    "inproceedings_address": inproceedings_address
                    }
                )
        db.session.commit()
    except Exception as exception:
        print("sources.py -> add_article:", exception)
        return False
    
    return True

def get_all_articles():
    if session.get("user_id") is None:
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
    print("sources.py / get_all_articles: articles_by_user = ", articles_by_user)
    
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
    print("sources.py / get_all_books: result = ", result)

    books_by_user = result.fetchall()
    print("sources.py / get_all_books: books_by_user = ", books_by_user)
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
    print("sources.py / get_all_inproceedings: inproceedings_by_user = ", inproceedings_by_user)

    return inproceedings_by_user


def delete_source(source_type, source_id):
    
    if session.get("user_id") is None:
        return False
    user_id = session["user_id"]

    
    allowed_source_types = ['books', 'articles', 'inproceedings']
    if source_type not in allowed_source_types:
        return False
    
    sql = text(f"DELETE FROM {source_type} WHERE (id = :id AND user_id=:user_id);")
    print("sources.py / delete_source: sql = ", sql, {"id": str(source_id), "user_id": str(user_id)})
    try:
        db.session.execute(sql, {"id": str(source_id), "user_id": str(user_id)})
        db.session.commit()

    except Exception as exception:
        print("sources.py -> delete_source:", exception)
        return False
    return True


# For testing:
def get_all(source_type, source_id):
    if session.get("user_id") is None:
        return False
    user_id = session["user_id"]
    
    allowed_source_types = ['books', 'articles', 'inproceedings']
    if source_type not in allowed_source_types:
        return None
    
    sql = text(f"SELECT * FROM {source_type} WHERE user_id = :user_id;")

    result = db.session.execute(sql, {"user_id": str(user_id)})
    print("sources.py / get_all_books: result = ", result)

    books_by_user = result.fetchall()
    print("sources.py / get_all_books: books_by_user = ", books_by_user)
    return books_by_user