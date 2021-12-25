from flask import flash, redirect, render_template, request, session, url_for

from . import app


@app.route("/")
def show_entries():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("entries/index.html")


@app.post("/login")
@app.get("/login")
def login():
    if request.method == "POST":
        if request.form["username"] != app.config["USERNAME"]:
            flash("ユーザ名が異なります")
        elif request.form["password"] != app.config["PASSWORD"]:
            flash("パスワードが異なります")
        else:
            session["logged_in"] = True
            flash("ログインしました")
            return redirect(url_for("show_entries"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("show_entries"))
