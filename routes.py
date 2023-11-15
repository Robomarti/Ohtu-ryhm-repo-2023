from app import app
from flask import render_template
from os import getenv
import sources


@app.route("/")
def index():
    return render_template("index.html")

#This is only for testing the database functions before ui
@app.route("/db_write_test")
def db_write_test():
    result = sources.add("Group 1", "HY", "Projektityö", "2023", "Readme", "12345", "Projektin readme", "1")
    print("routes.py / db_write_test: result = ", result)
    return ("Hello db_write_test!!")

@app.route("/db_read_test")
def db_read_test():
    data = sources.get_all()
    print("routes.py / db_read_test: data = ", data)
    return ("Hello db_read_test!! <p>Sources: <p>" + str(data))
