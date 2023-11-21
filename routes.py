from app import app
from flask import render_template, request, redirect, session
import sources


@app.route("/")
def index():
    if session.get["user_id"]:
        result = sources.get_all_articles()
        return render_template("index.html", references=result)
    else:
        redirect('/login')
    
@app.route("/add_reference", methods=["GET", "POST"])
def add_reference():
    if request.method == "GET":
        return render_template("add_reference.html")
    
    if request.method == "POST":
        print("add_reference: POST!")
        sources.add(
            request.form["author"], 
            request.form["organization"], 
            request.form["title"], 
            request.form["year"], 
            request.form["source_type"], 
            request.form["pages"], 
            request.form["doi"]
            )
        return redirect("/")
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        # if user already logged in then redirect
        if session.get("user_id"):
            return redirect("/")
        else:
            return render_template("login.html")

    if request.method == "POST":
        # log in user if success else render error
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            # users.py sets session["user_id"]
            return redirect("/")
        else:
            redirect("/login")


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
