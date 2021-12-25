from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from .. import app


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
