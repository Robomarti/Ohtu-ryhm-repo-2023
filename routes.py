from app import app
from flask import render_template, request, redirect
import sources


@app.route("/")
def index():
    result = sources.get_all()
    return render_template("index.html", references=result)
    
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
