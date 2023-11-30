# RUN TESTS OUTSIDE POETRY SHELL WITH COMMAND:
# FLASK_ENV=test poetry run pytest
# RUN COVERAGE IN POETRY SHELL:
# FLASK_ENV=test coverage run --branch -m pytest

import sys
import os

# If the following mess is not here, tests will not see app.py!!
# This will probably break if project folder structure is changed.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import unittest
from flask import session
from sqlalchemy.sql import text
from src.app import app  
from src.db import db 
import users

class UsersTestCase(unittest.TestCase):
    def setUp(self):
        app.config["SECRET_KEY"] = 'testkey1testkey2testkey3testkey4'
        app.test_request_context().push()

        with app.test_request_context():

            try: 
                sql = text("""CREATE TABLE users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_name TEXT,
                                password_hash TEXT
                            );""")

                db.session.execute(sql)
                db.session.commit()
            except Exception as exception:
                print("users_test.py -> setUp: Exception: ", exception)
            

    def tearDown(self):
        try: 
            sql = text("DROP TABLE users;")
            result = db.session.execute(sql)
            db.session.commit()
            print("users_test / tearDown: result =", result)
        except Exception as exception:
            print("users_test.py -> tearDown: Exception: ", exception)
            

    def test_register(self):
        with app.test_request_context():

            result = users.register("Test User 1", "TestPassword123!")
            self.assertEqual(result, True)

            sql = text("SELECT * FROM users;")
            result = db.session.execute(sql)
            data = result.fetchall()

            self.assertEqual(len(data), 1)
            self.assertEqual(data[0][1], 'Test User 1')
            self.assertEqual(session["user_id"], 1)

    def test_login(self):
        with app.test_request_context():

            result = users.register("Test User 1", "TestPassword123!")
            self.assertEqual(result, True)

            session.clear()

            result = users.login("Test User 1", "TestPassword123!")
            self.assertEqual(result, True)
            self.assertEqual(session["user_id"], 1)

    def test_login_with_wrong_password(self):
        with app.test_request_context():

            result = users.register("Test User 1", "TestPassword123!")
            self.assertEqual(result, True)

            session.clear()

            result = users.login("Test User 1", "TestPassword124!")
            self.assertEqual(result, False)
            self.assertEqual(session.get("user_id"), None)


    def test_logout(self):
        with app.test_request_context():

            users.register("Test User 1", "TestPassword123!")
            users.logout()

            self.assertEqual(session.get("user_id"), None)


if __name__ == '__main__':
    unittest.main()
