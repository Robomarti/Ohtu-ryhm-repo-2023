"""Contains functions for user account creation and logging in"""

from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from src.db import db

def register(username, password):
    """Creates a new account for a user"""    

    hash_value = generate_password_hash(password)

    try:
        sql = text("""INSERT INTO users (
                        user_name, 
                        password_hash)
                   VALUES (
                        :user_name,
                        :password_hash)""")
        
        db.session.execute(
            sql, {"user_name": username, "password_hash": hash_value})
        db.session.commit()
    except Exception as exception:
        print("users.py -> register: " , exception)
        return False

    return login(username, password)

def login(username, password):
    """Logs the user in"""    

    sql = text(
        """SELECT 
            id, 
            user_name, 
            password_hash 
        FROM 
            users 
        WHERE 
            user_name=:user_name""")
    
    result = db.session.execute(sql, {"user_name": username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            return True
        else:
            return False

def logout():
    """Logs the user out"""
    session.clear()

def user_id():
    """Returns the currently logged in user's id or 0 if no user is logged in"""
    return session.get("user_id", 0)