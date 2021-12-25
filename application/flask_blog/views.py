from flask import flash, redirect, render_template, request, session, url_for

from . import app


@app.route("/")
def show_entries():
    return render_template("entries/index.html")


@app.post("/login")
@app.get("/login")
def login():
    if request.method == "POST":
        if request.form["username"] != app.config["USERNAME"]:
            print("ユーザ名が異なります")
        elif request.form["password"] != app.config["PASSWORD"]:
            print("パスワードが異なります")
        else:
            return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def logout():
    return redirect("/")
