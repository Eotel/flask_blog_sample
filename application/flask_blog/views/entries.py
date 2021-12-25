from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from .. import app
from .. import db
from ..models.entries import Entry


@app.route("/")
def show_entries():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("entries/index.html")


@app.get("/entries/new")
def new_entry():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("entries/new.html")


@app.route("/entries", methods=["POST"])
def add_entry():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    entry = Entry(title=request.form["title"], text=request.form["text"])
    db.session.add(entry)
    db.session.commit()
    flash("新しい記事が作成されました")
    return redirect(url_for("show_entries"))
