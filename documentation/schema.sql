DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS articles CASCADE;
DROP TABLE IF EXISTS books CASCADE;
DROP TABLE IF EXISTS inproceedings CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    article_author TEXT, 
    article_title TEXT,
    article_journal TEXT,
    article_year INTEGER, 
    article_volume TEXT,
    article_number INTEGER,
    article_pages TEXT
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    book_author TEXT, 
    book_title TEXT,
    book_publisher TEXT,
    book_address TEXT,
    book_year INTEGER
);

CREATE TABLE inproceedings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    inproceedings_author TEXT, 
    inproceedings_title TEXT,
    inproceedings_booktitle TEXT,
    inproceedings_series TEXT,
    inproceedings_year INTEGER, 
    inproceedings_pages TEXT,
    inproceedings_publisher TEXT,
    inproceedings_address TEXT
);