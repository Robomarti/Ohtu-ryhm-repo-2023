from db import db
from sqlalchemy.sql import text

def add_article(article_author="", article_title="", article_journal="", article_year=2000, article_volume="", article_number=1, article_pages=""):
    owner_id = 1 #users.user_id() or session["user_id"]
    print("sources / add! author = ", article_author)
    sql = text("""INSERT INTO sources (
                        owner_id,
                        article_author, 
                        article_title, 
                        article_journal,
                        article_year,
                        article_volume,
                        article_number,
                        article_pages

                    ) 
                    VALUES (
                        :owner_id,
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
                                "owner_id": owner_id,
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
    except:
        print("sources.py / add: Exception!")
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
