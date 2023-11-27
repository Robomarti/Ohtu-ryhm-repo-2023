"""Creates the app and assigns it a secret_key variable from the .env file"""

from os import getenv
from flask import Flask

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

# we have to disable these pylint warnings since this order is
# the way flask wants us to import things
import src.routes # pylint: disable=unused-import, wrong-import-position
