from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("flask_blog.config")
from . import views  # noqa isort: skip

db = SQLAlchemy(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()


__all__ = ["views", "app", "db"]
