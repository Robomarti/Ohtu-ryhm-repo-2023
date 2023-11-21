from db import db
from sqlalchemy.sql import text

def add(author="", organization="", title="", year="2000", source_type="", pages="", doi=""):
    owner_id = 1 #users.user_id() or session["user_id"]
    print("sources / add! author = ", author)
    sql = text("""INSERT INTO sources (
                        author, 
                        organization, 
                        title, 
                        year, 
                        source_type, 
                        pages,
                        doi, 
                        owner_id
                    ) 
                    VALUES (
                        :author, 
                        :organization, 
                        :title, 
                        :year, 
                        :source_type, 
                        :pages,
                        :doi, 
                        :owner_id
                    )""")
    
    try:
        result = db.session.execute(sql, {"author": author, 
                                 "organization": organization, 
                                 "title": title, 
                                 "year": year, 
                                 "source_type": source_type, 
                                 "pages": pages, 
                                 "doi": doi, 
                                 "owner_id": owner_id
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
