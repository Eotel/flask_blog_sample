from datetime import datetime

from flask_sqlalchemy import DeclarativeMeta

from .. import db

BaseModel: DeclarativeMeta = db.Model


class Entry(BaseModel):
    __tablename__ = "entries"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, title=None, text=None) -> None:
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow()

    def __repr__(self) -> str:
        return "<Entry id:{} title:{} text:{}>".format(self.id, self.title, self.text)
