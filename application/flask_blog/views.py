from . import app


@app.route("/")
def show_entries():
    return "Hello World!"
