"""Creates the app and assigns it a secret_key variable from the .env file"""

from os import getenv , environ
from flask import Flask
import sys

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
if not getenv("SECRET_KEY"):
    print('NO SECRET KEY SET :<<', file=sys.stderr)
else:
    print('All is working :>', file=sys.stderr)

if environ.get("FLASK_ENV") == "test":
    print("Running in testing environment")
    import src.tests.robot.testing_routes

# we have to disable these pylint warnings since this order is
# the way flask wants us to import things
import src.routes # pylint: disable=unused-import, wrong-import-position
