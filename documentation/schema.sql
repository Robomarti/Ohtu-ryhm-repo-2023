CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name TEXT,
    password_hash TEXT
);

CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    user_id INT,
    article_author TEXT, 
    article_title TEXT,
    article_journal TEXT,
    article_year INT, 
    article_volume TEXT,
    article_number INT,
    article_pages TEXT
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    user_id INT,
    book_author TEXT, 
    book_title TEXT,
    book_publisher TEXT,
    book_address TEXT,
    book_year INT
);

CREATE TABLE inproceedings (
    id SERIAL PRIMARY KEY,
    user_id INT,
    inproceedings_author TEXT, 
    inproceedings_title TEXT,
    inproceedings_booktitle TEXT,
    inproceedings_series TEXT,
    inproceedings_year INT, 
    inproceedings_pages TEXT,
    inproceedings_publisher TEXT,
    inproceedings_address TEXT
);