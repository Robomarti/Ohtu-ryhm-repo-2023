from src.app import app
from src.db import db
from sqlalchemy.sql import text
from flask import session
from os import getenv, environ

# Testausta varten

def setup_db():
    if environ.get("FLASK_ENV") == "test":

        # Remove tables if they already exist
        try:
            sql = text("""DROP TABLE IF EXISTS books;""")
            db.session.execute(sql)
            sql = text("""DROP TABLE IF EXISTS articles;""")
            db.session.execute(sql)
            sql = text("""DROP TABLE IF EXISTS inproceedings;""")
            db.session.execute(sql)
            sql = text("""DROP TABLE IF EXISTS users;""")
            db.session.execute(sql)
            db.session.commit()
        except Exception as exception:
            print("AppLibrary.py -> create_tables : Exception: ", exception)

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
                print("AppLibrary.py -> create_tables : Exception: ", exception)

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
            print("AppLibrary.py -> create_tables : Exception: ", exception)

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
            db.session.commit()
        except Exception as exception:
            print("AppLibrary.py -> create_tables : Exception: ", exception)

        # Initialise test database for users
        try:
            sql = text("""CREATE TABLE users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_name TEXT,
                            password_hash TEXT
                        );""")
            db.session.execute(sql)
            db.session.commit()
        except Exception as exception:
            print("AppLibrary.py -> create_tables : Exception: ", exception)
