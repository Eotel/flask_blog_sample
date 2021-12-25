from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("flask_blog.config")
db = SQLAlchemy(app)

from .views import views  # isort: skip
from .views import entries  # isort: skip


@app.cli.command("init-db")
def init_db():
    db.create_all()


__all__ = ["views", "entries", "app", "db"]
