from datetime import datetime

from thermos import db

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text,nullable=False)
    date = db.Column(db.Date,default=datetime.utcnow)
    description = db.Column(db.String(300))

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(300),unique=True)