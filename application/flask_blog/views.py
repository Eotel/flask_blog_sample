from flask import flash, redirect, render_template, request, session, url_for

from . import app


@app.route("/")
def show_entries():
    return render_template("entries/index.html")
