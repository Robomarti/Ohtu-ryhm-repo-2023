"""Contains functions for user account creation and logging in"""

from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from src.db import db

def register(username, password):
    """Creates a new account for a user"""

    hash_value = generate_password_hash(password)

    try:
        username_exists = text("""SELECT user_name FROM users WHERE user_name=:user_name""")
        user = db.session.execute(username_exists, {"user_name": username}).fetchone()
        if user:
            return False

        sql = text("""INSERT INTO users (
                        user_name, 
                        password_hash)
                   VALUES (
                        :user_name,
                        :password_hash)""")

        db.session.execute(
            sql, {"user_name": username, "password_hash": hash_value})
        db.session.commit()

    # we disable this for now since we don't yet know what kind of
    # exceptions we should expect:
    # pylint: disable=broad-except
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
    if check_password_hash(user.password_hash, password):
        session["user_id"] = user.id
        return True
    return False

def logout():
    """Logs the user out"""
    session.clear()

def user_id():
    """Returns the currently logged in user's id or 0 if no user is logged in"""
    return session.get("user_id", 0)

#testing
def get_users():
    sql = text("SELECT * FROM users;")
    result = db.session.execute(sql)
    return result.fetchall()
