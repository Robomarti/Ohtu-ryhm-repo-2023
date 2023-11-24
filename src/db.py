from src.app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv, environ
import dotenv

if environ.get("FLASK_ENV") == "test":
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///:memory:'
else:
    dotenv.load_dotenv('.env')
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")

db = SQLAlchemy(app)
