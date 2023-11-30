from src import sources

def return_all_articles():
    articles = sources.get_all_articles()
    if articles is False:
        return []
    bibtex_articles = []

    for article in articles:
        bibtex_article = f"@article{{ {article.id},\n" \
                         f"  author = \"{article.article_author}\",\n" \
                         f"  title = \"{article.article_title}\",\n" \
                         f"  journal = \"{article.article_journal}\",\n" \
                         f"  year = {article.article_year},\n" \
                         f"  volume = \"{article.article_volume}\",\n" \
                         f"  number = \"{article.article_number}\",\n" \
                         f"  pages = \"{article.article_pages}\"\n" \
                         f"}}\n"
        bibtex_articles.append((bibtex_article, article.id))

    return bibtex_articles

def return_all_books():
    books = sources.get_all_books()
    if books is False:
        return []
    bibtex_books = []

    for book in books:
        bibtex_book = f"@book{{ {book.id},\n" \
                      f"  author = \"{book.book_author}\",\n" \
                      f"  title = \"{book.book_title}\",\n" \
                      f"  publisher = \"{book.book_publisher}\",\n" \
                      f"  address = \"{book.book_address}\",\n" \
                      f"  year = {book.book_year}\n" \
                      f"}}"
        bibtex_books.append((bibtex_book, book.id))

    return bibtex_books

def return_all_inproceedings():
    inproceedings = sources.get_all_inproceedings()
    if inproceedings is False:
        return []
    bibtex_inproceedings = []

    for inproceeding in inproceedings:
        bibtex_inproceeding = f"@inproceedings{{ {inproceeding.id},\n" \
                              f"  author = \"{inproceeding.inproceedings_author}\",\n" \
                              f"  title = \"{inproceeding.inproceedings_title}\",\n" \
                              f"  booktitle = \"{inproceeding.inproceedings_booktitle}\",\n" \
                              f"  series = \"{inproceeding.inproceedings_series}\",\n" \
                              f"  year = {inproceeding.inproceedings_year},\n" \
                              f"  pages = \"{inproceeding.inproceedings_pages}\",\n" \
                              f"  publisher = \"{inproceeding.inproceedings_publisher}\",\n" \
                              f"  address = \"{inproceeding.inproceedings_address}\"\n" \
                              f"}}\n"
        bibtex_inproceedings.append((bibtex_inproceeding, inproceeding.id))

    return bibtex_inproceedings
