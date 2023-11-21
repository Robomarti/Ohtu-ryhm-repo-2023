from db import db
from sqlalchemy.sql import text

def add_article(article_author: str, article_title: str, article_journal: str, article_year: int, article_volume: str, article_number: int, article_pages: str):
    user_id = 1 #users.user_id() or session["user_id"]
    print("sources.py / add! author = ", article_author)
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
                        :article_journal.
                        :article_year,
                        :article_volume,
                        :article_number,
                        :article_pages
                    )""")
    
    try:
        result = db.session.execute(sql, {
                                "user_id": user_id,
                                "article_author": article_author, 
                                 "article_title": article_title,
                                 "article_journal": article_journal,
                                 "article_year": article_year,
                                 "article_volume": article_volume,
                                 "article_number": article_number,
                                 "article_pages": article_pages
                                }
                            )
        db.session.commit()
    except Exception:
        print("sources.py -> add_article:" + Exception)
        return False
    
    return True

def add_book(book_author: str, book_title: str, book_publisher: str, book_address: str, book_year: int):
    user_id = 1 #users.user_id() or session["user_id"]
    print("sources.py / add! author = ", book_author)
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
                        :book_address,¨
                        :book_year
                    )""")
    
    try:
        result = db.session.execute(sql, {
                                "user_id": user_id,
                                "book_author": book_author, 
                                "book_title": book_title,
                                "book_publisher": book_publisher,
                                "book_address": book_address,
                                "book_year": book_year
                                }
                            )
        db.session.commit()
    except Exception:
        print("sources.py -> add_article:" + Exception)
        return False
    
    return True

def add_inproceedings(inproceedings_author: str, inproceedings_title: str, inproceedings_booktitle: str, inproceedings_series: str, inproceedings_year: int, inproceedings_pages: str, inproceedings_publisher: str, inproceedings_address: str):
    user_id = 1 #users.user_id() or session["user_id"]
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
                        inproceedings_booktitle,
                        :inproceedings_series,
                        :inproceedings_year,
                        :inproceedings_pages,
                        :inproceedings_publisher,
                        :inproceedings_address
                    )""")
    
    try:
        result = db.session.execute(sql, {
                                "user_id": user_id,
                                "inproceedings_author": inproceedings_author,
                                "inproceedings_title": inproceedings_title,
                                "inproceedings_booktitle": inproceedings_booktitle,
                                "inproceedings_series": inproceedings_series,
                                "inproceedings_year": inproceedings_year,
                                "inproceedings_pages": inproceedings_pages,
                                "inproceedings_publisher": inproceedings_publisher,
                                "inproceedings_address": inproceedings_address
                                }
                            )
        db.session.commit()
    except Exception:
        print("sources.py -> add_article:" + Exception)
        return False
    
    return True

def get_all_articles():
    user_id = 1 #users.user_id() or session["user_id"]

    sql = text("""SELECT 
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
    print("sources.py / get_all: result = ", result)

    sources_by_user = result.fetchall()
    return sources_by_user
