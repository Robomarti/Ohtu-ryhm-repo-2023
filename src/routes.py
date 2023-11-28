from flask import render_template, request, redirect, session

from src.app import app
import src.AppLibrary as applibrary
from src import sources, users

@app.route("/")
def index():
    if session.get("user_id"):
        articles = sources.get_all_articles()
        books = sources.get_all_books()
        inproceedings = sources.get_all_inproceedings()
        return render_template(
            "index.html", 
            articles=articles,
            books=books,
            inproceedings=inproceedings
            )
    return redirect('/login')

@app.route("/choose_source_type", methods=["GET", "POST"])
def choose_source():
    if request.method == "GET":
        if session.get("user_id"):
            return render_template("choose_source_type.html")
        return redirect("/login")

    if request.method == "POST":
        source_type = request.form.get('source_type')
        if source_type =='article':
            return render_template("add_article.html")
        if source_type =='book':
            return render_template("add_book.html")
        return render_template("add_inproceedings.html")
    return redirect("/")

@app.route("/add_reference", methods=["POST"])
def add_reference():
    if request.method == "POST":
        if request.form["source_type"] == "article":
            sources.add_article(
                request.form["author"],
                request.form["title"],
                request.form["journal"],
                request.form["year"],
                request.form["volume"],
                request.form["number"],
                request.form["pages"]
                )
        elif request.form["source_type"] == "book":
            sources.add_book(
                request.form["author"],
                request.form["title"],
                request.form["publisher"],
                request.form["address"],
                request.form["year"]
            )
        elif request.form["source_type"] == "inproceedings":
            sources.add_inproceedings(
                request.form["author"],
                request.form["title"],
                request.form["booktitle"],
                request.form["series"],
                request.form["year"],
                request.form["pages"],
                request.form["publisher"],
                request.form["address"]
            )
    return redirect("/")

@app.route("/delete_article/<ref_id>", methods=["POST"])
def delete_article(ref_id):
    sources.delete_source("articles", ref_id)
    return redirect("/")

@app.route("/delete_book/<ref_id>", methods=["POST"])
def delete_book(ref_id):
    sources.delete_source("books", ref_id)
    return redirect("/")

@app.route("/delete_inproceeding/<ref_id>", methods=["POST"])
def delete_inproceedings(ref_id):
    sources.delete_source("inproceedings", ref_id)
    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if session.get("register_error"):
            session.pop("register_error")
        if session.get("user_id"):
            return redirect("/")
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            # users.py sets session["user_id"]
            return redirect("/")
        return redirect("/login")
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        # if user already logged in then redirectd
        if session.get("user_id"):
            return redirect("/")
        return render_template("sign_in.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username, password):
            return redirect("/")
        session["register_error"] = "Username taken or invalid password"
        return redirect("/register")
    session.pop("register_error")
    return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/login")

@app.route("/db_initialize")
def db_initialize():
    applibrary.setup_db()
    data = users.get_users()
    print(data)
    return "Database should now be initialized\n"
